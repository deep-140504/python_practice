# thread pool executor with user defined threads
from concurrent.futures import ThreadPoolExecutor
import threading
import time

def worker(item):
    print("item", item)
    
    if item is None:  # Sentinel to terminate the thread
        return
    
    print(f"{threading.current_thread().name} processing {item}")
    time.sleep(1)  # Simulating task processing

# Create a ThreadPoolExecutor
num_threads = 3
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Submit tasks to the executor
    for i in range(5):  # Add actual tasks
        executor.submit(worker, i)
    
    # Submit sentinel values for each thread
    for _ in range(num_threads):
        executor.submit(worker, None)

print("All tasks processed, and threads terminated.")
