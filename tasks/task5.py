import asyncio
from asyncio import FIRST_COMPLETED


async def fast_task():
    return await asyncio.sleep(0.1, result='fast')


async def medium_task():
    return await asyncio.sleep(0.3, result='medium')


async def slow_task():
    return await asyncio.sleep(1, result='slow')


async def first_complete():
    tasks = [asyncio.ensure_future(task) for task in [
        fast_task(),
        medium_task(),
        slow_task()
    ]]
    done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)

    fist_result = next(iter(done)).result()

    for task in iter(pending):
        task.cancel()

    return fist_result
