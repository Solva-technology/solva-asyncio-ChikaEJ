import asyncio


async def fast_task():
    return await asyncio.sleep(0.1, result='fast')


async def medium_task():
    return await asyncio.sleep(0.3, result='medium')


async def slow_task():
    return await asyncio.sleep(1, result='slow')


async def first_complete():
    tasks = [asyncio.create_task(task) for task in [fast_task(),
                                                    medium_task(),
                                                    slow_task()]]
    done, pending = await asyncio.wait(tasks,
                                       return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        return task.result()
