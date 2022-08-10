import socket


def reactor(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print("Server up, running, and waiting for call on {0} {1}".format(host, port))

    try:
        while True:
            conn, cli_address = sock.accept()
            process_request(conn, cli_address)
    finally:
        sock.close()


def process_request(conn, cli_address):
    file = conn.makefile()

    print("Received connection from {0}".format(cli_address))

    try:
        while True:
            line = file.readline()
            if line:
                line = line.rstrip()
                if line == 'quit':
                    conn.sendall("connection closed\r\n")
                    return

                print("{0} -- > {1}".format(cli_address, line))
                conn.sendall("Echoed: {0}\r\n".format(line))
    finally:
        print("{0} quit".format(cli_address))
        file.close()
        conn.close()


if __name__ == "__main__":
    reactor('localhost', 8080)
