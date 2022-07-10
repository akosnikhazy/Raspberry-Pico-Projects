from machine import Pin
import utime

# using a stepper motor controller circuit for this
pins = [
    Pin(15,Pin.OUT), # IN1
    Pin(14,Pin.OUT), # IN2
    Pin(16,Pin.OUT), # IN3
    Pin(17,Pin.OUT)  # IN4
    ]

# all numbers in every line represent an electromagnet in the motor
# always one is active in this case so the motor goes around.
cw = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]
ccw = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
    ]

while True:
    for step in cw: # change cw to ccw if you want to see it go the other way here
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(0.001)
