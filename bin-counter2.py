# after a first one bunch of people told me its not that good
# so I felt the urge to make another. I still wanted to use
# list of bits.

# The last version: https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/bin-counter3.py

from machine import Pin
from time import sleep

def int_to_bin_list(int):
    bin = []
    while True:
        bin.append(int % 2)
        int = int // 2
        if int == 0: return list(reversed(bin))

# bit LEDs
bit_pins = [
    Pin(0,Pin.OUT),
    Pin(1,Pin.OUT),
    Pin(2,Pin.OUT),
    Pin(3,Pin.OUT),
    Pin(4,Pin.OUT),
    Pin(5,Pin.OUT),
    Pin(6,Pin.OUT),
    Pin(7,Pin.OUT)
]

counter = 0
while True:
    bin_list = int_to_bin_list(counter)
    bin_list_len = len(bin_list)
    for i in range(bin_list_len):
        bit_pins[8 - bin_list_len + i].value(bin_list[i])

    counter += 1
    if counter == 256:
        counter = 0
        for i in range(8):# reset the LEDs, you can lose this if you don't want it to go around, then just break here
            bit_pins[i].value(0)  
            
    # so we see what happens.
    sleep(0.25)
