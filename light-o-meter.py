from machine import Pin, ADC

# PIN 26 reads solar panel input
solarpanel = ADC(26)

# turn leds on and off
def switch_led(led):
    switcher = {
           "red":20,
           "yellow":19,
           "green":18
           
    }
    
    # turn all of them off
    Pin(18,Pin.OUT).value(0)
    Pin(19,Pin.OUT).value(0)
    Pin(20,Pin.OUT).value(0)
    
    # turn the one that we need now on
    if led != "none":
        Pin(switcher.get(led),Pin.OUT).value(1)
        
while True:
    # measure solar panel input
    measure = solarpanel.read_u16()* 3.3 / 65536;

    # weak light is less then one for my small solar panel
    if measure < 1:
        switch_led("red")
    else:
        # if its between 1 and 3 it is the yellow led
        if measure > 1 and measure < 2.9:
            switch_led("yellow")
        else:
            # if we have a lot of light it is green
            switch_led("green")
