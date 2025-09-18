#Write an example of an async function that fetches data from multiple URLs concurrently.
import asyncio
import aiohttp

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for i, result in enumerate(results, 1):
            print(f"URL {i} length:", len(result))

asyncio.run(main())
