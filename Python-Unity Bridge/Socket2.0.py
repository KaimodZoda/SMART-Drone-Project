import socket
import threading
import time

def send_command(command, s):
    s.sendall(command.encode())

# Dictionary to map user input to Unity commands
input_mapping = {
    'a': 'left',
    'd': 'right',
    'w': 'forward',
    's': 'backward'
}

# Establish a connection to Unity
unity_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
unity_socket.connect(("192.168.1.195", 12345))

last_input = 'stop'  # Initial command

def input_thread():
    global last_input
    while True:
        user_input = input("Enter a command (a, d, w, s): ").lower()
        if user_input in input_mapping:
            last_input = input_mapping[user_input]
        else:
            print("Invalid input. Please enter a valid command.")

# Start a separate thread for continuously sending commands
threading.Thread(target=input_thread, daemon=True).start()

# Continuously send the last command to Unity
while True:
    send_command(last_input, unity_socket)
    time.sleep(0.1)  # Adjust the sleep duration if needed
