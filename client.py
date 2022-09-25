import socket


def start_run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 1234))
        s.sendall(b"Hello, Socket")
        data = s.recv(1024)
        print("Received:", repr(data))


if __name__ == '__main__':
    start_run()
