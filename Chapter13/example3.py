import threading


def writer():
    global text

    while True:
        with service:
            resource.require()

        print("Writing being done by {0}".format(threading.current_thread().name))
        text += "Writing being done by {0}".format(threading.current_thread().name)

        resource.release()


def reader():
    global rcount

    while True:
        with service:
            rcounter.acquire()
            rcount += 1

            if rcount == 1:
                resource.acquire()

        rcounter.release()

        print("Reading being done by {0}".format(threading.current_thread().name))
        print(text)

        with rcounter:
            rcount -= 1
            if rcount == 0:
                resource.release()


text = "This is some text."
rcount = 0

rcounter = threading.Lock()
resource = threading.Lock()
service = threading.Lock()

threads = [threading.Thread(target=reader) for _ in range(3)] + [threading.Thread(target=writer) for _ in range(2)]

for thread in threads:
    thread.start()
