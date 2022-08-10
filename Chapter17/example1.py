import threading
import sys

sys.setswitchinterval(.000001)


def foo():
    global n
    n += 1


n = 0

threads = []

for i in range(1000):
    thread = threading.Thread(target=foo)
    threads.append(thread)

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Final value: {0}.".format(n))
print("Finished.")
