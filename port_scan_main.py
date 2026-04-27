import socket  # This allows python to create network connections
import port_functions

tgt_host, tgt_port = port_functions.user_input()
result = port_functions.connect(tgt_host, tgt_port)
print(f"The port {tgt_port} on {tgt_host} is {result}")
