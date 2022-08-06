import threading
import time


def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print('Thread {0} counting down {1}'.format(name, counter))
        counter -= 1


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting thread {0}".format(self.name))
        thread_count_down(self.name, self.delay)
        print("Finished thread {0}".format(self.name))
