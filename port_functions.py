import socket
import threading
import time
# add error handling for only port range numbers, and to make sure the end number is not smaller than the first number.


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

# This function is the actual check if a port is open or closed


def connect(th, tp):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((th, tp))
        return "Open"
    except:
        return "Closed"
    finally:
        client.close()


# This function is going to replace the for loops purpose of iterating through each of the port numbers and scanning
# thIs funcion basically takes uses the connect funtion and prints out the result
def scan_port(host, port):
    result = connect(host, port)
    print(f"Port {port} is {result}")
