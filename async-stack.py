import asyncio

stack = []

rangeMax = 3

async def pusher(value):
    stack.append(value)

async def popper(value):
    stack.pop()

async def main():
    counter = 0
    coroutines = []
    for i in range(rangeMax):
        coroutines.append(pusher(counter))
        counter += 1
    await asyncio.gather(*coroutines)
    for item in stack:
        print(item)

asyncio.run(main())
