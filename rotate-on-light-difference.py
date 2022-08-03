from machine import Pin, ADC
from time import sleep
import utime

# PIN 26 and 27 measures input voltage of solar panels
solarpanel1 = ADC(26)
solarpanel2 = ADC(27)

# the min diference between mesurements to trigger the motor
dif = 0.1

# time between steps of the motor
steptime = 0.001

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
    # measure the solar panel inputs
    measureNow1 = solarpanel1.read_u16()* 3.3 / 65536;
    measureNow2 = solarpanel2.read_u16()* 3.3 / 65536;
    
    # if the difference is bigger than this value
    if abs(measureNow1-measureNow2) > dif:
        # rotating the motor
        for step in motorsteps:
            for i in range(len(motorpins)):
                motorpins[i].value(step[i])
                utime.sleep(steptime)
    
    print("1: " + str(measureNow1))
    print("2: " + str(measureNow2))

    print("---")

