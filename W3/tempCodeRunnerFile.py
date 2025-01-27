
import asyncio

async def print_message():
    await asyncio.sleep(2)
    print("Python Exercises!")

async def main():
    await print_message()

asyncio.run(main())
