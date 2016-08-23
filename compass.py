# digital compass
# couldn't get this towork properly though
#
from microbit import *

# Image.ARROW_NW

# 360/8=45
# N  - 0-22 & 338-359
# NE - 23-66
# E  - 67-110
# SE - 111-155
# S  - 156-198
# SW - 199-243
# W  - 244-288
# NW - 289-338

# compass.calibrate()
while True:
    direction = compass.heading()
    if (direction >= 0 and direction <= 22):
        display.show(Image.ARROW_N)
    elif (direction >= 338 and direction <= 359):
        display.show(Image.ARROW_N)
    elif (direction >= 23 and direction <= 66):
        display.show(Image.ARROW_E)
    elif (direction >= 111 and direction <= 155):
        display.show(Image.ARROW_SE)
    elif (direction >= 156 and direction <= 198):
        display.show(Image.ARROW_S)
    elif (direction >= 199 and direction <= 243):
        display.show(Image.ARROW_SW)
    elif (direction >= 244 and direction <= 288):
        display.show(Image.ARROW_W)
    elif (direction >= 289 and direction <= 338):
        display.show(Image.ARROW_NW)
    # display.scroll(str(head))
    sleep(1000)
    
