# this does not have sentinel task done
import threading
from queue import Queue

def worker(q):
    while True:
        item = q.get()
        print("print", item)
        if item is None:  # Sentinel to terminate the thread
            break
        print(f"{threading.current_thread().name} processing {item}")
        q.task_done()

# Create a queue and add tasks
q = Queue()  # Correct import usage
for i in range(5):  # Add actual tasks
    q.put(i)

# Add sentinel values for each thread
num_threads = 3
for _ in range(num_threads):
    q.put(None)

# Start worker threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=worker, args=(q,), name=f"Worker-{i}")
    thread.start()
    threads.append(thread)

q.join()  # Wait until all tasks (excluding sentinels) are processed

# Join threads
for thread in threads:
    thread.join()

print("All tasks processed, and threads terminated.")

