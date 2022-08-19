# Raspberry-Pico-Projects
In this repo I collect my Raspberry Pi Pico code, I will list all of them in this README too.

## Table of contents
1. [Random Number Generator](#random-number-generator)
2. [Basic Stepper Motor controller](#basic-stepper-motor-controller)
3. [Stepper Motor forward and back](#stepper-motor-goes-forward-and-back)
4. [Stepper Motor Reverse Movement on Button Press](#stepper-motor-reverse-movement-on-button-press)
5. [Rotate Stepper Motor on Light Difference](#rotate-stepper-motor-on-light-difference)
6. [Light-o-Meter](#light-o-meter)
7. [Bin-Counter](#bin-counter)


## Random Number Generator

([real-random-number.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/real-random-number.py)) 

This small python script to work needs a voltage input from PIN26 from a solar panel. The randomness comes from the measurement of the power provided by the Sun. As you can not predict the Sun, you can not predict the numbers, hence it is more random than any pseudo-random programming function.

This is my very basic setup: solar panel's + on PIN26, - on one of the GND. If you use bigger solar panel protect your board!
![Raspberry Pico with solar panel](https://raw.githubusercontent.com/akosnikhazy/Raspberry-Pico-Projects/main/readme-images/random-number-generator.jpg)

## Basic Stepper Motor controller
([basic-stepper-motor.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/basic-stepper-motor.py))

A very basic stepper motor script I used to test how it all works. It is based on [this video](https://www.youtube.com/watch?v=gyqOETtpINg). The video didn't help me understand how to turn the motor in another way. Then I understood the numbers [0,0,0,1] represent the electromagnets in the motor. So the order you turn them on makes it move in one way or the another.

## Stepper Motor Goes Forward and Back
([stepper-forward-and-back.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/stepper-forward-and-back.py))

By reversing the step list runtime you can make the motor go in the other way. First I thought about using a flag and and `if` to use two set of steps. But reversing the array runtime make it step perfect. Also more elegant and the code is shorter.

## Stepper Motor Reverse Movement on Button Press
([stepper-motor-with-buttons.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/stepper-motor-with-buttons.py))

This script reverses the stepper motor's movement on any of the two buttons press. The idea is the motor will have an arm that presses any of the two buttons while rotating this way it can not go more than 360° so the cables attached to the motor won't spool.

The setup is easy. You connect the buttons to pins 12 and 13 and ground. The motor is connected to the Pico with stepper motor controller on pins 14,15,16,17 and the controllers gots power from the Pico's 3v3out pin (also its - is on a Pico's GND)

![Raspberry Pico with solar panel](https://raw.githubusercontent.com/akosnikhazy/Raspberry-Pico-Projects/main/readme-images/stepper-motor-with-buttons.jpg)

## Rotate Stepper Motor on Light Difference
([rotate-on-light-difference.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/rotate-on-light-difference.py))

This is a mix of two other projects. Please read the [Random Number Generator](#random-number-generator)'s description about how to connect the solar panel to the Pico. The only difference is this uses two solar panels, so you have to do the same with PIN27 too. The idea is to rotate the motor toward the light so it gets maximum power input.

## Light-o-Meter
([light-o-meter.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/light-o-meter.py))

This simple script turns on a red, a green, or a yellow LED based on the voltage input of the solar panel. Pin 18, 19 and 20 are the LEDs. Pin 28 measures the solar panel's voltage. As I use a small and weak solar panel I got from a calculator, I did not protect the board from it, but if you use a stronger one please be safe with it.

![The Light-o-Meter](https://raw.githubusercontent.com/akosnikhazy/Raspberry-Pico-Projects/main/readme-images/light-o-meter.jpg)

## Bin Counter
([bin-counter.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/bin-counter.py))
([bin-counter2.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/bin-counter2.py))
([bin-counter3.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/bin-counter3.py))
([bin-counter3.py](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/bin-counter4.py))

This is a binary counter, because I have LEDs and wanted to make something simple. It turned out there is no zfill in MicroPython so I worked around that padding list with list. It is not the best solution for sure. Setup is simple: PINs 0-7 are LEDs.

The second one is a better version, without making string bin() string form numbers. I straight away make a list and toggle the LEDs based on that.

The third version I dropped the bin function, built it in the main loop and switch LEDs on creting the binary number

The third was the last version but then I realized I do not need the list of pins :)
![Binary Counter in action](https://raw.githubusercontent.com/akosnikhazy/Raspberry-Pico-Projects/main/readme-images/bin-counter.gif)
