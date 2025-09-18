 Advanced Networking & System Design
73.What is WSGI, and why is it important?
WSGI (Web Server Gateway Interface) is a standard Python interface between web servers (e.g., gunicorn, uWSGI) and Python web applications/frameworks (e.g., Django, Flask).
Importance:
Decouples web servers from application code.
Allows interoperability: any WSGI server can serve any WSGI app.


74. How do you scale a Python web application to handle millions of requests?
Key strategies (multi-layered):
Horizontal scaling: run many app instances behind a load balancer (K8s, ELB).
Use async / non-blocking I/O: handle more concurrent connections per process (ASGI + uvicorn).
Process workers: multiple processes (gunicorn workers) per CPU core.
Autoscaling: cloud autoscaling groups or K8s HPA.
Cache aggressively: Redis/memcached for DB results, pages, session data, CDN for static assets.
Database scaling: read replicas, sharding, connection pooling.
Message queues: offload expensive work to workers (Celery/RQ/Kafka consumers).
Backpressure / rate limiting: protect resources under load.
Optimize code: profile hot paths, reduce allocations, use compiled extensions (Cython) if needed.
Observability: metrics, tracing, logs to find bottlenecks.
Use CDN & edge: reduce origin load for static and cached content.
Scaling to “millions” is a system-design problem: combine horizontal scale, non-blocking IO, caching, and robust infra.

75. What are Python’s options for message queues (e.g., RabbitMQ, Kafka)?
Common message systems used with Python:
RabbitMQ — broker with reliable messaging, good for task queues.
Apache Kafka — distributed log, great for high-throughput streaming and event sourcing.
Redis Streams — lightweight streaming on top of Redis.
Amazon SQS — managed queue (cloud).
NATS / Pulsar — alternatives for specialized needs.
Python client libs: pika (RabbitMQ), confluent-kafka or kafka-python (Kafka), redis-py (Redis Streams), boto3 (SQS).

76. How do you implement a distributed task queue in Python (like Celery)?
Typical approach:
Choose broker (Redis/RabbitMQ) and backend (Redis, database) for results.
Define tasks and a worker process that consumes tasks.
Minimal Celery example:
# tasks.py
from celery import Celery
app = Celery("proj", broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")
@app.task
def add(a, b):
    return a + b
Run worker:
celery -A tasks worker --loglevel=info
Call asynchronously:
res = add.delay(2,3)
res.get()  # blocks until complete (or use callbacks)
Alternatives: RQ (Redis Queue), Dramatiq, or custom consumers reading Kafka/Redis.

77. What is the difference between sync and async web frameworks in Python?
Sync frameworks (e.g., Flask, Django classic): request handlers are blocking. To scale, you add processes/threads per concurrent connection.
Async frameworks (e.g., FastAPI, Starlette, Sanic, aiohttp): handlers use async def and await to do non-blocking I/O, allow a single worker to handle many concurrent requests when I/O-bound.
Tradeoffs:
Async shines when you have many I/O-bound concurrent tasks (APIs, websockets).
Sync is simpler and often fine for CPU-bound or lower concurrency use cases.
Async requires async-aware libraries (DB drivers, HTTP clients) to gain benefits.

78. How do you handle retries and backoff in Python services?
Pattern: retry failed operations with exponential backoff and jitter. Use libraries to avoid reimplementing:
tenacity — popular retry lib (supports sync/async).
Manual pattern: exponential delay sleep = base * 2**n + jitter.
Example with tenacity:
from tenacity import retry, stop_after_attempt, wait_exponential_jitter
@retry(stop=stop_after_attempt(5), wait=wait_exponential_jitter(1, 10))
def unreliable_call():
    # do network call; raise on failure
    ...
Also consider idempotency, circuit-breakers, and avoiding retry storms.

79. What is the role of uvicorn and gunicorn in Python web apps?
gunicorn — a WSGI HTTP server for Python (sync apps). It manages worker processes and listening sockets.
uvicorn — a lightning-fast ASGI server (async), used to run async frameworks like FastAPI or Starlette.
They are application servers; you typically put them behind an external reverse proxy / load balancer (nginx, cloud LB).
Note: gunicorn can run ASGI apps via worker class uvicorn.workers.UvicornWorker (so you get gunicorn process management + uvicorn async runtime).

80. How do you implement rate limiting in a Python API?
Common techniques:
Token bucket or leaky bucket algorithm.
Central store (Redis) to keep counters across processes/instances.
Per-IP / per-user keys with TTLs.
Use libraries/middlewares (e.g., limits, ratelimit, Flask-Limiter, or FastAPI middleware).
Simple Redis token-bucket pseudocode:
# conceptual (not production hardened)
# key = f"rate:{user_id}"
# tokens, last_ts stored; refill tokens based on elapsed time
# or simpler: increment key with TTL
current = redis.incr(key)
if current == 1:
    redis.expire(key, window_seconds)
if current > allowed:
    return 429
For production:
Use sliding-window or fixed-window with Redis LUA for atomicity.
Consider burst allowance, penalty windows, and adding distributed rate-limiters or API gateway features (Cloudflare, Kong).

87. How do you sandbox untrusted Python code?
Difficult (CPython isn’t designed for safe sandboxing). Some approaches:
Run code in a separate process/container/VM (best).
Restrict environment (limited globals/locals in exec).
Use libraries like RestrictedPython (limited subset of Python).
For true isolation: Docker containers, Firejail, or specialized sandboxes.

88. How do you secure a Python application against code injection attacks?
Never use eval/exec on untrusted input.
Use parameterized queries in SQL (cursor.execute("SELECT ... WHERE id=%s", (id,))).
Sanitize inputs for shell calls, or use subprocess.run([...], shell=False).
For templates, use safe engines (Jinja2 with autoescaping).
Principle of least privilege (restrict what code can do).
Escape untrusted data before embedding in HTML/SQL/commands.

89. How do you optimize Python for multi-core CPUs given the GIL?
The GIL (Global Interpreter Lock) prevents true parallel execution of Python bytecode in threads.
Options:
Multiprocessing (multiprocessing.Process or concurrent.futures.ProcessPoolExecutor) → separate processes, one per core.
C extensions / NumPy / Numba → release GIL during heavy computation in C.
Cython → compile parts of code, bypassing GIL.
Alternative interpreters (Jython, IronPython, PyPy STM).
Async IO for concurrency (but not CPU-bound parallelism).