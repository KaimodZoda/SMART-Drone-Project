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
        if arduino_message in coordinates:
            x, y = coordinates[arduino_message]
            move_mouse(x, y, arduino_message)
            last_message_time[0] = time.time()  # Update the time of the last message
        update_interface(arduino_message)
    elif time.time() - last_message_time[0] > 0.06:  # If no message received within 51 ms
        pyautogui.mouseUp()  # Trigger mouse up
    root.after(51, check_updates)  # Check again after 50 milliseconds

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

last_message_time = [0]  # List to store the time of the last message

def move_mouse(x, y, arduino_message):
    if arduino_message in ["Up", "Down", "Forward"]:
        pyautogui.mouseUp()  # Corrected call to pyautogui.mouseUp()
        pyautogui.moveTo(x, y)  
        pyautogui.mouseDown()
        time.sleep(0.05)  # You might adjust this sleep duration
        pyautogui.mouseUp()
    else:
        pyautogui.moveTo(x, y)  
        pyautogui.mouseDown()  # Only mouse down without mouse up

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
