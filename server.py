import socket
import threading


def handle_client(c, addr):
    with c:
        print(addr, "connected.")

        while True:
            data = c.recv(1024)
            if not data:
                break
            c.sendall(data)
    print(addr, "disconnected.")


def start_listen():
    print("Start to listen...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 0.0.0.0 for any network interface card
        s.bind(("0.0.0.0", 1234))
        s.listen()

        while True:
            c, addr = s.accept()

            t = threading.Thread(target=handle_client, args=(c, addr))
            t.start()


if __name__ == '__main__':
    start_listen()
