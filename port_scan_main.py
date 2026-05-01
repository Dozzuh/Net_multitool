import socket  # This allows python to create network connections
import threading
import time
import port_functions


tgt_host, tgt_port, end_port = port_functions.user_input()

threads = []

# For loop job will switch to creating threads rather than iterating through each port to scan
# changes from scanning ports to creating instances of scanning the port
for x in range(tgt_port, end_port + 1):
    thread = threading.Thread(
        target=port_functions.scan_port, args=(tgt_host, x))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    # result = port_functions.connect(tgt_host, x)
    # print(f"The port {x} on host {tgt_host} is {result}")
