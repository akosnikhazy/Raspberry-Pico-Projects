# pong game
# it has no reset and players can spam the button (or just keep them pressed :D)
# I just made this as a concept, wouldn't spend more time with it.

from machine import Pin
from time import sleep

players = [
    Pin(12,Pin.IN,Pin.PULL_UP),
    Pin(13,Pin.IN,Pin.PULL_UP)
]

field = [
    Pin(8,Pin.OUT), # left goal
    Pin(0,Pin.OUT),
    Pin(1,Pin.OUT),
    Pin(2,Pin.OUT),
    Pin(3,Pin.OUT),
    Pin(4,Pin.OUT),
    Pin(5,Pin.OUT),
    Pin(6,Pin.OUT),
    Pin(7,Pin.OUT),
    Pin(9,Pin.OUT) # right goal
]



ball_pos = 1
tick = 0.5
play = False


def ini():
    play = False
    ball_pos = 1

ini();

while True:
    if not play: # start the game or continue
        if not players[0].value():
            play = True
        else:
            continue
        
    # controls
    if ball_pos == 9:
        if not players[1].value():
            print("player 2 hit")
            field.reverse()
            ball_pos = 0
            
        if not players[0].value():
            print("player 1 hit")
            field.reverse()
            ball_pos = 0
            
    # game logic. If the ball is out it stops, if not it goes through the field    
    if ball_pos > 9:
        field[9].value(1)
    else:
        fieldposcount = 1
        for i in field:
            i.value(0)
            if fieldposcount == ball_pos:
                i.value(1)
            fieldposcount += 1
        
        ball_pos += 1
    
    sleep(tick)
