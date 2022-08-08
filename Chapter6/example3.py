from multiprocessing import Process, current_process
import time
import os


def print_info(title):
    print(title)

    if hasattr(os, 'getppid'):
        print("Parent process id: {0}".format(str(os.getppid())))

    print("Current process ID: {0}".format(str(os.getpid())))


def f():
    print_info('Function f')

    pname = current_process().name
    print("Staring process {0}".format(pname))
    time.sleep(1)
    print("Ending process {0}".format(pname))


if __name__ == '__main__':
    print_info("Main program")

    p = Process(target=f)
    p.start()
    p.join()

    print('Done.')
