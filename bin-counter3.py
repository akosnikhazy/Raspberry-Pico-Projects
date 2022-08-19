# Third and last version of the bin-counter series. This one
# dropped the bin converter function, and instantly switches
# the LEDs

# Update: not the last. https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/bin-counter4.py

from machine import Pin
from time import sleep

# bit LEDs
bit_pins = [
    Pin(7, Pin.OUT),
    Pin(6, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(0, Pin.OUT)
]
now = 0
counter = 0
while True:
    now = counter
    bit = 0
    while now > 0:
        bit_pins[bit].value(now % 2)
        bit += 1
        now = now // 2
         
    counter += 1
    if counter == 256:
        counter = 0
        for i in range(8):  # reset the LEDs, you can lose this if you don't want it to go around, then just break here
            bit_pins[i].value(0)

    # so we see what happens.
    sleep(0.25)
