from machine import Pin
import utime

pins = [
    Pin(15,Pin.OUT),
    Pin(14,Pin.OUT),
    Pin(16,Pin.OUT),
    Pin(17,Pin.OUT)
    ]

steptime = 0.01
counter = 0.0;
maxcount = 128

steps = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

while True:
    for step in steps:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(steptime)
            
    if counter >=maxcount:
        counter = 0
        steps.reverse()           
    counter = counter + 1
