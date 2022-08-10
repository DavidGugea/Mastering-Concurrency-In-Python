import threading
import time
from concurrent.futures import ThreadPoolExecutor


class LockedCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, x):
        with self.lock:
            new_value = self.value + x
            time.sleep(0.001)
            self.value = new_value

    def get_value(self):
        with self.lock:
            value = self.value

        return value


counter = LockedCounter()
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(counter.increment, [1 for i in range(300)])

print("Final counter: {0}".format(counter.get_value()))
print("Finished.")
