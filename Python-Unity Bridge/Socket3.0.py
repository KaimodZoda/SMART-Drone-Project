import socket
import threading
import time
import keyboard

def send_command(command, s):
    s.sendall(command.encode())

# Dictionary to map user input to Unity commands
input_mapping = {
    '1': 'left',
    '3': 'right',
    '5': 'forward',
    '2': 'backward',
    '9': 'up',
    '6': 'down',
}

# Establish a connection to Unity
unity_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
unity_socket.connect(("192.168.1.42", 12345))

last_input = 'stop'  # Initial command

def input_thread():
    global last_input
    while True:
        for key, command in input_mapping.items():
            if keyboard.is_pressed(key):
                last_input = command
                time.sleep(0.2)  # Add a small delay to avoid multiple rapid inputs

# Start a separate thread for continuously sending commands
threading.Thread(target=input_thread, daemon=True).start()

# Continuously send the last command to Unity
while True:
    send_command(last_input, unity_socket)
    time.sleep(0.1)  # Adjust the sleep duration if needed
