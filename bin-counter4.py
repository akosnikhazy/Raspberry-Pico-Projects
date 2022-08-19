# bonus round: no list of pins, just set the pins
from machine import Pin
from time import sleep

now = 0
counter = 0
while True:
    now = counter
    bit = 7
    while now > 0:
        Pin(bit,Pin.OUT).value(now % 2)
        bit -= 1
        now = now // 2
         
    counter += 1
    if counter == 256:
        counter = 0
        for i in range(8):  # reset the LEDs, you can lose this if you don't want it to go around, then just break here
            Pin(i,Pin.OUT).value(0)

    # so we see what happens.
    sleep(0.01)
