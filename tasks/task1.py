import asyncio

import aiohttp


async def fetch_status(session, url):
    async with session.get(url) as response:
        return response.status


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        return await asyncio.gather(*tasks)
