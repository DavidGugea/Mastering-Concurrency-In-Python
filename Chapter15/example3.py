import time
import threading
from multiprocessing import Pool

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    start = time.perf_counter()
    countdown(COUNT)

    print("Sequential program finished.")
    print("Took {0:.2f} seconds.".format(time.perf_counter() - start))
    print()

    thread1 = threading.Thread(target=countdown, args=(COUNT // 2, ))
    thread2 = threading.Thread(target=countdown, args=(COUNT // 2,))

    start = time.perf_counter()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Multithreading program finished.")
    print("Took {0:.2f} seconds".format(time.perf_counter() - start))
    print()

    pool = Pool(processes=2)
    start = time.perf_counter()
    pool.apply_async(countdown, args=(COUNT//2, ))
    pool.apply_async(countdown, args=(COUNT // 2,))
    pool.close()
    pool.join()

    print("Multiprocessing program finished.")
    print("Took {0:.2f} seconds".format(time.perf_counter() - start))
