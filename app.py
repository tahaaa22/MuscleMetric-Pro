import socket

# Define the Bluetooth address of the device you want to connect to
target_address = "60-E3-2B-58-6B-C7" # Replace with the Bluetooth address of your device

# Define the port number to connect to on the device
port = 1  # Standard Bluetooth port

# Create a Bluetooth socket
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Connect to the device
sock.connect((target_address, port))

# Send data to the device
data = 'Hello, Bluetooth!'
sock.send(data.encode())

# Receive data from the device
received_data = sock.recv(1024)
print('Received:', received_data.decode())

# Close the socket connection
sock.close()