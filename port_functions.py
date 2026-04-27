import socket


def user_input():
    target_host = input("Enter a web address: ")
    # i need error handling for non integer inputs
    target_port = int(input("Enter a port number: "))
    return target_host, target_port


def connect(th, tp):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((th, tp))
        client.close()
        return "Open"
    except:
        client.close()
        return "Closed"
