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



#############################################################################
#code for pressing takeoff
#########################################################################################
# pyautogui.moveTo(x_takeoff, y_takeoff)

# pyautogui.mouseDown()
# time.sleep(1)

#pyautogui.mouseUp()
# time.sleep(1)


######################################################################################
#code for move up
#########################################################################
# pyautogui.moveTo(x_coordinateup, y_coordinateup)

# pyautogui.mouseDown()

# time.sleep(hold_duration)

# pyautogui.mouseUp()


##############################################################
#code for move down
######################################
# pyautogui.moveTo(x_coordinatedown, y_coordinatedown)


# pyautogui.mouseDown()

# time.sleep(hold_duration)

# pyautogui.mouseUp()


###############################################################
#code for move left
################################################333
# pyautogui.moveTo(x_coordinateleft, y_coordinateleft)

# pyautogui.mouseDown()

# time.sleep(hold_duration)

# pyautogui.mouseUp()

###############################################################
#code for move right
##############################################################
# pyautogui.moveTo(x_coordinateright, y_coordinateright)


# pyautogui.mouseDown()

# time.sleep(hold_duration)

# pyautogui.mouseUp()

#####################################################
#code for move front
##############################################################
# pyautogui.moveTo(x_coordinatefront, y_coordinatefront)

# pyautogui.mouseDown()

# time.sleep(hold_duration)

# pyautogui.mouseUp()

#####################################################
#code for move back
##############################################################

# pyautogui.moveTo(x_coordinateback, y_coordinateback)

# pyautogui.mouseDown()

# time.sleep(hold_duration)

# pyautogui.mouseUp()



############################################################
#playground
#############################################################


pyautogui.moveTo(x_coordinateup, y_coordinateup)
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp()

pyautogui.mouseDown()

# time.sleep(2)

pyautogui.mouseUp()


time.sleep(5)



pyautogui.moveTo(x_coordinateleft, y_coordinateleft)

pyautogui.mouseDown()

time.sleep(2)

pyautogui.mouseUp()

pyautogui.moveTo(x_coordinateright, y_coordinateright)

pyautogui.mouseDown()

time.sleep(2)

pyautogui.mouseUp()

pyautogui.moveTo(x_coordinatefront, y_coordinatefront)

pyautogui.mouseDown()

time.sleep(2)

pyautogui.mouseUp()

pyautogui.moveTo(x_coordinateback, y_coordinateback)


pyautogui.mouseDown()

time.sleep(2)

pyautogui.mouseUp()

pyautogui.moveTo(x_coordinatedown, y_coordinatedown)


pyautogui.mouseDown()

time.sleep(hold_duration)

pyautogui.mouseUp()

print("Done holding click.")

###########################################################################
##########################################################################