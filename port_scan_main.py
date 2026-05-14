import socket  # This allows python to create network connections
import threading
import time
import port_functions


tgt_host, tgt_port, end_port = port_functions.user_input()

threads = []  # creates an empty list that will later be used to store each thread

found_open = False

# The below loop, creates a thread with the plan to run scan_port, starts the thread, and adds it to the list.
for x in range(tgt_port, end_port + 1):
    thread = threading.Thread(
        target=port_functions.scan_port, args=(tgt_host, x))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()  # this tells the parent thread to wait for the child threads to complete before moving on

for port in sorted(port_functions.results):
    if port_functions.results[port][1] == "Open":
        found_open = True
        print(
            f"Port {port} is {port_functions.results[port][1]} - {port_functions.results[port][0]}")
if not found_open:
    print("Ports not open")
