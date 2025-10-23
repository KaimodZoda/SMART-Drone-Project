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

# Establish a connection to Unity
unity_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
unity_socket.connect(("172.20.10.7", 12345))

def arduino_thread():   
    while True:
        if ser.in_waiting > 0:
            arduino_message = ser.readline().decode('utf-8').rstrip()
            if arduino_message in arduino_mapping:
                command = arduino_mapping[arduino_message]
                send_command(command, unity_socket)
                print("Received message from Arduino:", arduino_message)

# Start a separate thread for continuously receiving Arduino messages
ser = serial.Serial('COM15', 38400)  # Change 'COM3' to the port your Arduino is connected to
threading.Thread(target=arduino_thread, daemon=True).start()

# Continuously read gestures from the Arduino and update the Unity command
while True:
    time.sleep(0.05)  # Adjust the sleep duration if needed
