import random
import time
import threading


def update():
    global counter

    with count_lock:
        current_counter = counter
        time.sleep(random.randint(0, 1))
        counter = current_counter + 1


counter = 0
count_lock = threading.Lock()

threads = [threading.Thread(target=update) for _ in range(20)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Final counter: {0}".format(counter))
print("Finished.")
