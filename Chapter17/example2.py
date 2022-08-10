import threading
import sys

sys.setswitchinterval(.000001)


def foo():
    global my_list
    my_list.append(1)


my_list = []

threads = []

for i in range(1000):
    thread = threading.Thread(target=foo)
    threads.append(thread)

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Final list length: {0}.".format(len(my_list)))
print("Finished.")
