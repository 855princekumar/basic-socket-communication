import socket                                   # Import necessary modules
import time                                     # For time-related functionalities
from threading import Timer                     # For scheduling background tasks

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

s.bind(('', 5000))                               # Bind the socket to a specific address and port (empty string for host address, port 5000)

s.listen(5)                                      # Listen for incoming connections with a maximum queue size of 5

print('Server is now running...')                # Print a message indicating that the server is running

def background_controller():                     # Define a function for background processing
    message = 'Hello client'                      # Define a message to be sent to the client
    print(message)                                # Print the message to the console
    clientsocket.send(bytes(message, "utf-8"))   # Send the message to the connected client after encoding it to bytes using UTF-8
    Timer(5, background_controller).start()      # Schedule the function to run again after 5 seconds

while True:                                      # Main loop to accept incoming connections
    clientsocket, address = s.accept()            # Accept a connection and get the client socket and address
    print(f"Connection from {address} has been established.")  # Print a message indicating that a connection has been established
    background_controller()                      # Call the background_controller function to handle background processing
