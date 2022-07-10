from machine import Pin
import utime

pins = [
    Pin(15,Pin.OUT),
    Pin(14,Pin.OUT),
    Pin(16,Pin.OUT),
    Pin(17,Pin.OUT)
    ]

steptime = 0.001
counter = 0.0;
timelimit = 2;

mode = "cw"; # can be cw or ccw

steps = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

while True:
    for step in steps:
        for i in range(len(pins)):
            if counter > timelimit:
                counter = 0
                steps.reverse() # with this you make it rotate backwards
            
            pins[i].value(step[i])
            utime.sleep(steptime)
            counter = counter + steptime
           
            

