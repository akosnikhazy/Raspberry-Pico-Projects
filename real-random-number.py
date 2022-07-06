# By measuring voltage from a sun collector
# you get real random numbers that cannot
# be predicted

# setup: https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/random-number-generator.JPG
# just put the + of a sun collector to PIN26 and the - to one of the GND-s.
# (please keep in mind the Pico's input voltage limits, use caution and protect the board if needed,
# I use a small suncollector I got from a calculator to test this idea out)


from machine import Pin, ADC
from time import sleep

# PIN 26 measures input voltage
suncollector = ADC(26)

# choose these smartly if your sun collector never
# goes beyond these values; the result can't be
# normalized properly
min = 0.5
max = 0.5

while True:
    measureNow = suncollector.read_u16()* 3.3 / 65536;
     
    if measureNow < min:
        min = measureNow
    
    if measureNow > max:
        max = measureNow
        
    # you will get a number between 0 and 100    
    normalized = (measureNow-min)/(max-min)*100
    
    print(normalized)
    sleep(0.25)
