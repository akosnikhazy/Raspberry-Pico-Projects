# disclaimer: this is far from the best, most optimal solution. It is just a solution. 
# The point of this whole repository is me learning Raspberry Pico and MicroPython. 
# I write every code on the fly. Then later I try to optimize and rewrite.

from machine import Pin
from time import sleep

# our bits
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
    
    # list of bits converted from int to bin to string
    num_now = list(str(bin(counter)[2:]))
    
    # zfill is not present in micropython :)
    padding_list = []
    for i in range(0,8-len(num_now)):
       padding_list.append('0');
       
    # so I padding the list instead with another list made up from zeroes
    num_now = padding_list + num_now
    
    # so I can use this loop to switch leds on PINs
    for i in range(len(num_now)):
        bit_pins[i].value(int(num_now[i]))
    
    # we grow the counter by one and restart if we are at limit. 8 bits is 255 max
    counter += 1
    if counter == 256:
        counter = 0
    
    # so we see what happens.
    sleep(0.25)
