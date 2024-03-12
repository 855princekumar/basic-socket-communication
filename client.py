import socket                                   # Import necessary module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

s.connect(("replace_with_the_server_ip", 5000))              # Connect to the server with the specified IP address and port (192.168.28.82, port 5000)

while True:                                     # Main loop for continuous communication
    print(s.recv(1024).decode("utf-8"))        # Receive data (up to 1024 bytes), decode it from bytes to UTF-8, and print it to the console
