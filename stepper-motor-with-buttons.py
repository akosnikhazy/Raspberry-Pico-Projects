# this script reverse the stepper motors movement
# if any of the two buttons are pressed. It waits
# a little before it can be reveresed again.

# button pins are 12 and 13
# motor pins are 14 15 16 17

from machine import Pin
import utime

# time between steps of the motor
steptime = 0.001

# when the button is pressed the motor changes direction
# we wait maxcount counter until it can change direction
# again. We need this because if the button is pressed
# too long it will change direction back
counter = 0
maxcount = 30

# the two buttons
buttons = [
    Pin(12,Pin.IN,Pin.PULL_UP),
    Pin(13,Pin.IN,Pin.PULL_UP)
]

motorpins = [
    Pin(15,Pin.OUT),
    Pin(14,Pin.OUT),
    Pin(16,Pin.OUT),
    Pin(17,Pin.OUT)
]

motorsteps = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

while True:
    # rotating the motor
    for step in motorsteps:
        for i in range(len(motorpins)):
            motorpins[i].value(step[i])
            utime.sleep(steptime)
    
    # if any of the buttons are pressed and we are not turning
    if (not buttons[0].value() or not buttons[1].value()) and counter == 0:
        counter = counter + 1
        motorsteps.reverse()        
    
    # if we are turning back wait a little before we can turn again
    if counter > 0:
        counter = counter + 1
        if counter >= maxcount:
            counter = 0
