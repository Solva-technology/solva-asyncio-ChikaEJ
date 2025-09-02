import asyncio


async def limited_worker(task_id, semaphore):
    async with semaphore:
        return await asyncio.sleep(0.1, result=task_id)


async def limited_runner():
    semaphore = asyncio.Semaphore(2)
    tasks = [limited_worker(i, semaphore) for i in range(5)]
    return await asyncio.gather(*tasks)
