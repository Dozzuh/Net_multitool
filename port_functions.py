import socket
import threading
import time
# add error handling for only port range numbers, and to make sure the end number is not smaller than the first number.

thread_limiter = threading.Semaphore(10)
results = {}
lock = threading.Lock()


def user_input():
    target_host = input("Enter a web address: ")
    while True:
        try:
            start_port = int(
                input("Enter the start of the port range to scan: "))
            end_port = int(input("Enter the end range of the port to scan: "))
            return target_host, start_port, end_port
        except:
            print("Not a valid port number.\nValid port numbers are 0-65535")


def connect(th, tp):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    try:
        client.connect((th, tp))
        return "Open"
    except:
        return "Closed"
    finally:
        client.close()


# This function limits the amount of threads made, takes the output of connect()
# stores it in result, then stores the key/value pair in to a dictionary called results
def scan_port(host, port):
    with thread_limiter:
        result = connect(host, port)
        with lock:
            results[port] = result
