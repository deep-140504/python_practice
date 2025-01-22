import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


# Normal code
# func(4)
# func(3)
# at this time, all these are running independently
# instead these can be run concurrently using the threading module of python

# same code using the thread
time1 = time.perf_counter()
t1 = threading.Thread(target = func, args=[4])
t2 = threading.Thread(target = func, args=[3])
t3 = threading.Thread(target = func, args=[2])
print()
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
# by calling join what happens, is rest of the code, below it will wait for the completion of task till the execution of threads are not completed, so before calling the join on the threads, time taken was nearly zero seconds, but now the time taken will be 4, as the total time taken = slowest process, which is 4 in this case

# threds can be used in cases where the process is I/O bound and not the CPU bound
time2 = time.perf_counter()
print(f"Total time consumed{time2 - time1} seconds") 