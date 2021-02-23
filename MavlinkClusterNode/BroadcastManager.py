import socket
import time
import threading


def _server_thread():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    message = b"your very important message"
    for _ in range(10):
        server.sendto(message, ("255.255.255.255", 37020))
        print("message sent!", flush=True)
        time.sleep(1)


def _client_thread():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 37020))
    for _ in range(10):
        data, addr = client.recvfrom(1024)
        print("received message: %s" % data)


def start_threads():
    server_thread = threading.Thread(target=_server_thread)
    client_thread = threading.Thread(target=_client_thread)

    server_thread.start()
    client_thread.start()
