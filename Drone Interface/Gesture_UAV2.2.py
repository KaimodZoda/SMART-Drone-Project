import pyautogui
import time
import serial
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Function to update the interface with received messages
def update_interface(message):
    current_time = time.strftime("%H:%M:%S")  # Get the current time
    formatted_message = f"{current_time}: {message}"  # Format the message with time
    textbox.insert(tk.END, formatted_message + "\n")
    textbox.see(tk.END)  # Scroll to the bottom

# Function to continuously check for updates from the secondary thread
def check_updates():
    if ser.in_waiting > 0:
        arduino_message = ser.readline().decode('utf-8').rstrip()
        if "Detected gestures:" not in arduino_message:  # Filter out "Detected gesture:" message
            update_interface(arduino_message)
            process_message(arduino_message)
    root.after(50, check_updates)  # Check again after 50 milliseconds


# Function to process the received message
def process_message(message):
    global prev_message
    if prev_message == message:
        if message in coordinates:
            x, y = coordinates[message]
            move_mouse(x, y, message)
    else:
        if prev_message and prev_message != "":
            # If the previous message is different and not an empty string
            pyautogui.mouseUp()
        prev_message = message

# Create the main Tkinter window
root = tk.Tk()
root.title("Serial Communication Interface")
root.geometry("400x300")
root.wm_attributes("-topmost", True)  # Make the window always on top

# Create a scrolled text box to display messages
textbox = ScrolledText(root, wrap=tk.WORD)
textbox.pack(fill=tk.BOTH, expand=True)

# Auto GUI mouse positions + durations
coordinates = {
    'Left': (1200, 720),
    'Right': (1600, 720),
    'Forward': (1400, 520),
    'Backward': (1400, 920),
    'Up': (500, 520),
    'Down': (490, 940),
}

prev_message = ""  # Variable to store the previous message

def move_mouse(x, y, arduino_message):
    pyautogui.mouseUp()  # Trigger mouse up
    pyautogui.moveTo(x, y)  
    pyautogui.mouseDown()
    time.sleep(0.05)  # You might adjust this sleep duration
    pyautogui.mouseUp()

# Start a separate thread for continuously receiving Arduino messages
ser = serial.Serial('COM15', 38400)  # Change to the port your MCU is connected to and change baudrate to the programmed value
threading.Thread(target=check_updates, daemon=True).start()

# Function to handle window events
def handle_events():
    root.update()
    root.after(50, handle_events)

# Start handling window events
handle_events()

# Start the Tkinter event loop
root.mainloop()
