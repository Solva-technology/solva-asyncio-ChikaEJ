import asyncio


async def safe_divide(a: float, b: float) -> float or str:
    try:
        await asyncio.sleep(0.1)
        return a / b
    except ZeroDivisionError:
        return 'Ошибка деления'


async def run_divisions():
    tasks = [safe_divide(10.0, num) for num in [2, 0, 5]]
    return await asyncio.gather(*tasks)
