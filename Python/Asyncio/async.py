import asyncio
#
# async def say_hello() -> None:
#     await asyncio.sleep(2)
#     print("Hello")
#
# async def say_bye() -> None:
#     await asyncio.sleep(1)
#     print("Bye")
#
# async def main():
#     task_1 = asyncio.create_task(say_hello())
#     task_2 = asyncio.create_task(say_bye())
#     await task_1
#     await task_2
#
#
# asyncio.run(main())

async def send_one() -> None:
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        if n % 3 != 0:
            print(f"Прошло {n} сек")
async def send_three() -> None:
    while True:
        await asyncio.sleep(3)
        print("Прошло еще 3 секунды")

async def main() -> None:
    task_1 = asyncio.create_task(send_one())
    task_2 = asyncio.create_task(send_three())

    await task_2
    await task_1

if __name__ == '__main__':
    asyncio.run(main())

