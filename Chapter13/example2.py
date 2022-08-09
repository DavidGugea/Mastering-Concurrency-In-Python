import threading


def writer():
    global text
    global wcount

    while True:
        with wcounter:
            wcount += 1
            if wcount == 1:
                read_try.acquire()

        with resource:
            print("Writing being done by {0}".format(threading.current_thread().name))
            text += "Writing was done by {0}".format(threading.current_thread().name)

        with wcounter:
            wcount -= 1
            if wcount == 0:
                read_try.release()


def reader():
    global rcount

    while True:
        with read_try:
            with rcounter:
                rcount += 1
                if rcount == 1:
                    resource.acquire()

            print("Reading being done by {0}".format(threading.current_thread().name))
            print(text)

            with rcounter:
                rcount -= 1
                if rcount == 0:
                    resource.release()


text = "This is some text."
wcount = 0
rcount = 0

wcount = threading.Lock()
rcounter = threading.Lock()
resource = threading.Lock()
read_try = threading.Lock()

threads = [threading.Thread(target=reader) for _ in range(3)] + [threading.Thread(target=writer) for _ in range(2)]

for thread in threads:
    thread.start()
