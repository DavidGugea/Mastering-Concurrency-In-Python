import threading
import random
import time

random.seed(0)


def update(pause_period):
    global counter

    with count_lock:
        current_counter = counter
        time.sleep(pause_period)
        counter = current_counter + 1


pause_periods = [random.randint(0, 1) for _ in range(20)]

counter = 0
count_lock = threading.Lock()

start = time.perf_counter()
for i in range(20):
    update(pause_periods[i])

print("--Sequential version--")
print("Final counter: {0}".format(counter))
print("Took {0:.2f} seconds.".format(time.perf_counter() - start))

counter = 0
threads = [threading.Thread(target=update, args=(pause_periods[i],)) for i in range(20)]

start = time.perf_counter()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("--Concurrent version--")
print("Final counter: {0}".format(counter))
print("Took {0:.2f} seconds.".format(time.perf_counter() - start))

print("Finished.")
