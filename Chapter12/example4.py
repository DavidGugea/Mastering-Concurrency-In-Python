import threading
from typing import List


class Acquire:
    def __init__(self, *locks):
        self.locks: List[threading.Lock] = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        for lock in reversed(self.locks):
            lock.release()

        return False


def philosopher(left, right):
    while True:
        with Acquire(left, right):
            print(f"Philosopher at {threading.current_thread()} is eating.")
