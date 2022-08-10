import time
import threading

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


start = time.perf_counter()
countdown(COUNT)

print("Sequential program finished.")
print("Took {0:.2f} seconds.".format(time.perf_counter() - start))

thread1 = threading.Thread(target=countdown, args=(COUNT // 2,))
thread2 = threading.Thread(target=countdown, args=(COUNT // 2,))

start = time.perf_counter()
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Concurrent program finished.")
print("Took {0:.2f} seconds".format(time.perf_counter() - start))
