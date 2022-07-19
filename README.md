# Raspberry-Pico-Projects
In this repo I collect my Raspberry Pi Pico code, I will list all of them in this README too.

## Table of contents
1. [Random Number Generator](#random-number-generator)
2. [Basic Stepper Motor controller](#basic-stepper-motor-controller)
3. [Stepper Motor forward and back](#stepper-motor-goes-forward-and-back)


## Random Number Generator

([real-random-number.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/real-random-number.py)) 

This small python script to work needs a voltage input from PIN26 from a solar panel. The randomness comes from the measurement of the power provided by the Sun. As you can not predict the Sun, you can not predict the numbers, hence it is more random than any pseudo-random programming function.

This is my very basic setup: solar panel's + on PIN26, - on one of the GND. If you use bigger solar panel protect your board!
![Raspberry Pico with solar panel](https://raw.githubusercontent.com/akosnikhazy/Raspberry-Pico-Projects/main/random-number-generator.JPG)

## Basic Stepper Motor controller
([basic-stepper-motor.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/basic-stepper-motor.py))

A very basic stepper motor script I used to test how it all works. It is based on [this video](https://www.youtube.com/watch?v=gyqOETtpINg). The video didn't help me understand how to turn the motor in another way. Then I understood the numbers [0,0,0,1] represent the electromagnets in the motor. So the order you turn them on makes it move in one way or the another.

## Stepper Motor Goes Forward and Back
([stepper-forward-and-back.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/stepper-forward-and-back.py))

By reversing the step list runtime you can make the motor go in the other way. First I thought about using a flag and and `if` to use two set of steps. But reversing the array runtime make it step perfect. Also more elegant and the code is shorter.

## Stepper Motor reverse movement on button press
([stepper-motor-with-buttons.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/stepper-motor-with-buttons.py))

This script reverse the stepper motor's movement on any of the two button's press. The idea is the motor will have an arm that presses any of the two buttons while rotating this way it can not go more than 360° so the cables attached to the motor wont spool.

