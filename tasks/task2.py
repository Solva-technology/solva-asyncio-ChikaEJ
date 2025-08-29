import asyncio


async def delayed_echo(text, delay):
    return await asyncio.sleep(delay, result=text)


async def echo_all():
    tasks = [delayed_echo(text, 5) for text in ['hello', 'world', '!']]
    return await asyncio.gather(*tasks)
