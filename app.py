import bluetooth

# Address of the Bluetooth module connected to your Arduino
target_address = "60-E3-2B-58-6B-C7" # Replace with the Bluetooth module's address

# Create a Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Connect to the Bluetooth module
sock.connect((target_address, 1))

try:
    while True:
        # Receive data from the Bluetooth module
        data = sock.recv(1024)
        print("Received:", data)

except KeyboardInterrupt:
    # Close the Bluetooth socket on Ctrl+C
    sock.close()
