import pyautogui
import time

x_coordinateup = 500
y_coordinateup = 520

x_coordinatedown = 490
y_coordinatedown = 940

x_coordinateleft = 1200
y_coordinateleft = 720

x_coordinateright = 1600
y_coordinateright = 720


x_coordinatefront = 1400
y_coordinatefront = 520

x_coordinateback = 1400
y_coordinateback = 920

x_takeoff = 100
y_takeoff = 1000


hold_duration = 10

def detect_input(input_sequence):
    # Iterate over the input sequence
    for item in input_sequence:
        if item is None or item.strip() == "":
            print("Default")
            pyautogui.mouseUp()
        elif item == "up":
            print("Up detected")
            pyautogui.moveTo(x_coordinateup, y_coordinateup)
            pyautogui.mouseDown()
            time.sleep(0.05)
            pyautogui.mouseUp()
        elif item == "left":
            print("Left detected")
            pyautogui.moveTo(x_coordinateleft, y_coordinateleft)
            pyautogui.mouseDown()
        elif item == "down":
            print("Down detected")
            pyautogui.moveTo(x_coordinatedown, y_coordinatedown)
            pyautogui.mouseDown()
        time.sleep(0.05)  # Introduce a 50 ms delay between each print

# Example input
input_sequence = ["up", "up", "up", "left", "left", "down", "down"]

# Call the function
iterations = 0
while iterations < 1:
    detect_input(input_sequence)
    iterations += 1


