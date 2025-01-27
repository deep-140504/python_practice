# this has locks
import threading
from queue import Queue

def worker(q, lock):
    while True:
        item = None
        with lock:  # Ensure that only one thread accesses the queue at a time
            item = q.get()

        print("item", item)
        
        if item is None:  # Sentinel to terminate the thread
            with lock:  # Acquire lock before marking sentinel task as done
                q.task_done()  # Mark the sentinel as done
            break
        
        print(f"{threading.current_thread().name} processing {item}")
        
        with lock:  # Acquire lock before marking task as done
            q.task_done()

# Create a queue and add tasks
q = Queue()  # Correct import usage
for i in range(5):  # Add actual tasks
    q.put(i)

# Add sentinel values for each thread
num_threads = 3
for _ in range(num_threads):
    q.put(None)

# Create a lock
lock = threading.Lock()

# Start worker threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=worker, args=(q, lock), name=f"Worker-{i}")
    thread.start()
    threads.append(thread)

q.join()  # Wait until all tasks (excluding sentinels) are processed

# Join threads
for thread in threads:
    thread.join()

print("All tasks processed, and threads terminated.")
