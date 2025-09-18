#Advanced Networking & System Design
#71.Simple REST API without Flask/Django
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"msg":"Hello World"}).encode())

httpd = HTTPServer(('localhost', 8000), SimpleAPI)
print("Server running on port 8000")
httpd.serve_forever()
#72.Implement WebSockets
import asyncio
import websockets

async def echo(ws, path):
    async for message in ws:
        await ws.send(f"Echo: {message}")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, "localhost", 8765))
asyncio.get_event_loop().run_forever()
#73.WSGI
def app(environ, start_response):
    start_response('200 OK',[('Content-Type','text/plain')])
    return [b'Hello WSGI']
#78.Handling retries & backoff
from tenacity import retry, wait_exponential

@retry(wait=wait_exponential(multiplier=1, min=1, max=10))
def unreliable_call():
    pass
#80.Rate limiting
import time, redis
r=redis.Redis()

def allow_request(user_id, limit=5, window=60):
    key=f"user:{user_id}"
    now=int(time.time())
    r.zadd(key,{now:now})
    r.zremrangebyscore(key,0,now-window)
    if r.zcard(key)>limit:
        return False
    return True