from machine import Pin, ADC
from time import sleep

measure = ADC(26)

leds = [
    Pin(0,Pin.OUT),
    Pin(1,Pin.OUT),
    Pin(2,Pin.OUT),
    Pin(3,Pin.OUT),
    Pin(4,Pin.OUT),
    Pin(5,Pin.OUT),
    Pin(6,Pin.OUT),
    Pin(7,Pin.OUT),
]

maximum = 1.2
minimum = 0.1

while True:
   
   for x in leds:
      x.value(0)
   
   measurement = measure.read_u16()* 3.3 / 65536

   zi = (measurement - minimum) / (maximum - minimum) * 100
   
   # very lazy
   if zi > 12.5:
       leds[0].value(1)
       
   if zi > 25:
       leds[1].value(1)
       
   if zi > 37.5:
       leds[2].value(1)
       
   if zi > 50:
       leds[3].value(1)
       
   if zi > 61.5:
       leds[4].value(1)
       
   if zi > 75:
       leds[5].value(1)
       
   if zi > 87.5:
       leds[6].value(1)
       
   if zi > 90:
       leds[7].value(1)
