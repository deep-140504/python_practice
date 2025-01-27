from concurrent.futures import ThreadPoolExecutor
from math import ceil
import time
def partial_factorial(start, end):
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product

def multi_threaded_factorial(n, num_threads):
    chunk_size = ceil(n / num_threads)

    with ThreadPoolExecutor() as executor: 
    # with ThreadPoolExecutor(max_worker = num_threads) as executor: 
        # the thing to take into consideration is that, if you do not explicitly provides max_worker, than python will internally handle the max workers required, so no need to bother about
        futures = []
        for i in range(num_threads): 
            start = i * chunk_size + 1
            end = min((i + 1) * chunk_size, n)
            # futures.append(partial_factorial, start, end) this is wrong, call executor.submit and pass the same as argument
            futures.append(executor.submit(partial_factorial, start, end))

        final_result = 1
        for future in futures:
            final_result *= future.result()
        return final_result

n = 100
num_threads = 3

start = time.perf_counter()

factorial_result = multi_threaded_factorial(n, num_threads)
print(f"the factorial of {n} is {factorial_result}")

end = time.perf_counter()

print(end - start)


import asyncio

async def print_message():
    await asyncio.sleep(2)
    print("Python Exercises!")

async def main():
    await print_message()

asyncio.run(main())
