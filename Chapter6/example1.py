from multiprocessing import Process
import time


def count_down(name, delay):
    print("Process {0} starting".format(name))

    counter = 5

    while counter:
        time.sleep(delay)
        print("Process {0} counting down: {1}".format(name, counter))
        counter -= 1

    print("Process {0} exiting".format(name))


if __name__ == '__main__':
    process1 = Process(target=count_down, args=('A', 0.5))
    process2 = Process(target=count_down, args=('B', 0.5))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Done.')
