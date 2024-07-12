import asyncio
from random import random

# coroutine to simulate cooking food
async def cook_food(name):
    time_to_cook = 1 + random()
    print(f'Microwave ({name}): Cooking {time_to_cook:.17f} seconds...')
    await asyncio.sleep(time_to_cook)
    print(f'Microwave ({name}): Finished cooking')
    return name, time_to_cook

# main coroutine
async def main():
    # create tasks for cooking different foods
    tasks = [
        asyncio.create_task(cook_food("Rice")),
        asyncio.create_task(cook_food("Noodle")),
        asyncio.create_task(cook_food("Curry")),
    ]

    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # get the first completed task result
    for task in done:
        first_completed, time_taken = task.result()
        print(f'Completed task: 1\n - {first_completed} is completed in {time_taken:.17f}')

    # print details of pending tasks
    print(f'Uncompleted task: {len(pending)}')
    for task in pending:
        name, _ = await task
        print(f' - {name} is still pending')

# start the asyncio program
asyncio.run(main ())
