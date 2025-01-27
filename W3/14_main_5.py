# thread pool executor with dynamic threads, number of threads managed by the thread pool executor, so no need to bother about it, no sentinel values required
from concurrent.futures import ThreadPoolExecutor
import threading
import time

start = time.perf_counter()

def worker(item):
    # print("item", item)
    print(f"{threading.current_thread().name} processing {item}")
    # time.sleep(1)  # Simulate task processing time

# Create a ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    # Submit tasks to the executor
    for i in range(5):  # Add actual tasks
        executor.submit(worker, i)

# No need for sentinel values, the threads will automatically finish when all tasks are processed.
print("All tasks processed, and threads terminated.")

end = time.perf_counter()
print(f"Total time taken: {end - start}")