import socket

def send_command(command, s):
    s.sendall(command.encode())
    response = s.recv(1024)
    print(response.decode())

# Dictionary to map user input to Unity commands
input_mapping = {
    'a': 'left',
    'd': 'right',
    'w': 'forward',
    's': 'backward'
}

# Establish a connection to Unity
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.1.42", 12345))

    while True:
        user_input = input("Enter a command (a, d, w, s): ").lower()

        if user_input in input_mapping:
            unity_command = input_mapping[user_input]
            send_command(unity_command, s)
        else:
            print("Invalid input. Please enter a valid command.")
