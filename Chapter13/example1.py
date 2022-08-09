import threading


def writer():
    global text

    while True:
        with resource:
            print("Writing being done by {0}".format(threading.current_thread().name))
            text += "Writing was done by {0}".format(threading.current_thread().name)


def reader():
    global rcount

    while True:
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


text = 'This is some text.'
rcount = 0
rcounter = threading.Lock()
resource = threading.Lock()

threads = [threading.Thread(target=reader) for _ in range(3)] + [threading.Thread(target=writer) for _ in range(2)]

for thread in threads:
    thread.start()
