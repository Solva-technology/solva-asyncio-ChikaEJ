import asyncio


async def delayed_echo(text, delay):
    await asyncio.sleep(delay)
    return text


async def echo_all():
    tasks = [delayed_echo(text, 5) for text in ['hello', 'world', '!']]
    return await asyncio.gather(*tasks)
