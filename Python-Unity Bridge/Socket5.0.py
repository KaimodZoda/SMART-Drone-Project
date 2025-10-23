import socket
import serial
import threading
import time

def send_command(command, s):
    s.sendall(command.encode())

# Dictionary to map Arduino messages to Unity commands
arduino_mapping = {
    'Left': 'left',
    'Right': 'right',
    'Forward': 'forward',
    'Backward': 'backward',
    'Up': 'up',
    'Down': 'down',
    # Add more conditions as needed
}

# Function to establish the connection to Unity
def connect_to_unity():
    unity_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    unity_socket.connect(("192.168.1.42", 12345))
    return unity_socket

# Establish a connection to Unity in a separate thread
unity_socket = connect_to_unity()

# Initialize serial connection
ser = serial.Serial('COM15', 38400, timeout=1)  # Set timeout here, adjust as needed

def arduino_thread(unity_socket):
    last_receive_time = time.time()  # Track the last time data was received
    while True:
        if ser.in_waiting > 0:
            arduino_message = ser.readline().decode('utf-8').rstrip()
            last_receive_time = time.time()  # Update the last receive time
            if arduino_message in arduino_mapping:
                command = arduino_mapping[arduino_message]
                send_command(command, unity_socket)
                print("Received message from Arduino:", arduino_message)
            else:
                print("Unknown message from Arduino:", arduino_message)
        elif time.time() - last_receive_time >= 0.050:
            send_command("stop", unity_socket)
            last_receive_time = time.time()  # Reset the last receive time after sending "stop"
            time.sleep(0.05)  # Adjust the sleep duration if needed

# Start a separate thread for continuously receiving Arduino messages
threading.Thread(target=arduino_thread, args=(unity_socket,), daemon=True).start()
