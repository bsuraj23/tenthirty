# tiny_loop.py
import selectors
import socket
import types
import time
import heapq
from collections import deque

# --- Future & Task ---------------------------------------------------------
class Future:
    def __init__(self):
        self._done = False
        self._result = None
        self._callbacks = []

    def done(self):
        return self._done

    def result(self):
        if not self._done:
            raise RuntimeError("Future not done")
        return self._result

    def set_result(self, res):
        if self._done:
            raise RuntimeError("Future already done")
        self._done = True
        self._result = res
        for cb in self._callbacks:
            cb(self)

    def add_done_callback(self, cb):
        if self._done:
            cb(self)
        else:
            self._callbacks.append(cb)


class Task(Future):
    def __init__(self, coro, loop):
        super().__init__()
        self._coro = coro  # generator-based coroutine
        self._loop = loop
        # Start the task
        self._loop._ready.append(self._step)

    def _step(self, fut=None):
        try:
            if fut is None:
                to_await = self._coro.send(None)
            else:
                to_await = self._coro.send(fut.result())
        except StopIteration as stop:
            self.set_result(getattr(stop, "value", None))
            return
        except Exception as e:
            # propagate exception as result (simple handling)
            self.set_result(e)
            return

        # to_await might be a Future or a special awaitable created by loop
        if isinstance(to_await, Future):
            to_await.add_done_callback(self._step)
        else:
            # If it's something else (None), schedule next step
            self._loop.call_soon(self._step)

# --- Event loop ------------------------------------------------------------
class TinyLoop:
    def __init__(self):
        self._selector = selectors.DefaultSelector()
        self._ready = deque()             # callables ready to run
        self._timers = []                 # heap of (when, counter, callback)
        self._timer_counter = 0
        self._stopping = False

    # --- scheduling primitives
    def call_soon(self, callback):
        self._ready.append(callback)

    def call_later(self, delay, callback):
        when = time.monotonic() + delay
        self._timer_counter += 1
        heapq.heappush(self._timers, (when, self._timer_counter, callback))

    # --- I/O integration
    def add_reader(self, fd, callback):
        self._selector.register(fd, selectors.EVENT_READ, callback)

    def remove_reader(self, fd):
        try:
            self._selector.unregister(fd)
        except Exception:
            pass

    # --- task API
    def create_task(self, coro):
        return Task(coro, self)

    def run_until_complete(self, fut):
        # If fut is a coroutine, wrap in Task
        if isinstance(fut, types.GeneratorType):
            fut = self.create_task(fut)

        # main loop
        while not fut.done() and not self._stopping:
            # process ready callbacks
            while self._ready:
                cb = self._ready.popleft()
                try:
                    cb()
                except Exception as e:
                    print("Exception in callback:", e)

            # run due timers
            now = time.monotonic()
            while self._timers and self._timers[0][0] <= now:
                _, _, cb = heapq.heappop(self._timers)
                self._ready.append(cb)

            # decide selector timeout
            timeout = None
            if self._ready:
                timeout = 0
            elif self._timers:
                timeout = max(0, self._timers[0][0] - time.monotonic())

            # wait for I/O or timeout
            if timeout is None:
                events = self._selector.select()
            else:
                events = self._selector.select(timeout)

            for key, mask in events:
                callback = key.data
                # schedule the callback to run soon
                self._ready.append(lambda cb=callback: cb())

        return fut.result()

    def stop(self):
        self._stopping = True

# --- helpers / awaitables --------------------------------------------------
def sleep(delay):
    fut = Future()
    def done(_=None):
        fut.set_result(None)
    # We'll schedule this via loop when someone awaits sleep
    # So sleeper will call loop.call_later
    fut._schedule = (delay, done)  # attach scheduling info
    return fut

def read_ready(sock):
    fut = Future()
    def on_ready(_=None):
        fut.set_result(None)
    fut._sock = sock
    fut._schedule = on_ready
    return fut

# --- Example usage ---------------------------------------------------------
# Example: a coroutine that uses sleep
def coro_sleep_demo():
    print("start sleep demo")
    yield from awaitable(sleep, 1)   # sleep 1s
    print("woke up after 1s")
    yield from awaitable(sleep, 0.5)
    print("woke again after 0.5s")
    return "done-sleep"

# Utility to bridge our primitive `sleep` function to generator-style "await"
def awaitable(factory, *args, **kwargs):
    # factory returns Future with scheduling info (we rely on loop to schedule)
    fut = factory(*args, **kwargs)
    # The caller awaits the future. But we must ensure the loop schedules it.
    # So we yield a small wrapper that, when scheduled, will register the timer/reader.
    current_loop = global_loop
    if hasattr(fut, "_sock"):
        # register for read
        current_loop.add_reader(fut._sock, fut._schedule)
    elif hasattr(fut, "_schedule") and isinstance(fut._schedule, tuple):
        delay, cb = fut._schedule
        current_loop.call_later(delay, cb)
    else:
        # immediate
        current_loop.call_soon(fut._schedule)
    # yield the future so the Task will add a done callback
    yield fut
    # after resume, return the future.result (we don't use it)
    return fut.result()

# Example: simple TCP echo server using selectors
def echo_server(host="127.0.0.1", port=25000):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.setblocking(False)
    srv.bind((host, port))
    srv.listen()
    print("echo server listening on", (host, port))

    def accept_cb():
        try:
            conn, addr = srv.accept()
        except BlockingIOError:
            return
        conn.setblocking(False)
        print("accepted", addr)
        # register per-connection callback
        def conn_cb():
            try:
                data = conn.recv(4096)
            except BlockingIOError:
                return
            if not data:
                print("closing", addr)
                loop.remove_reader(conn)
                conn.close()
                return
            # echo back (blocking send may be fine for small demos)
            conn.sendall(data)
        loop.add_reader(conn, conn_cb)

    loop.add_reader(srv, accept_cb)
    # Keep server running for a while, then stop
    def stop_later():
        print("stopping server after 10s")
        loop.stop()
    loop.call_later(10, stop_later)
    # block until loop.stop or server finishes
    # We return a Future that completes when loop stops; for simplicity just sleep
    yield from awaitable(sleep, 10)
    return "server-stopped"

# Entrypoint ---------------------------------------------------------------
if __name__ == "__main__":
    loop = TinyLoop()
    # expose global_loop used in awaitable()
    global_loop = loop

    # Run the sleep demo and the echo server concurrently
    t1 = loop.create_task(coro_sleep_demo())
    t2 = loop.create_task(echo_server())
    res = loop.run_until_complete(t2)  # run until server stops
    print("server finished:", res)
