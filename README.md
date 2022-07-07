# Raspberry-Pico-Projects
Im thos repo I collect my Raspberry Pi Pico code, I will list all of them in this README too.

# Random Number Generator (real-random-number.py)
[This](https://github.com/akosnikhazy/Raspberry-Pico-Projects/blob/main/real-random-number.py) small python script to work needs a voltage input from PIN26 from a solar panel. The randomness comes from the measurement of the power provided by the Sun. As you can not predict the Sun, you can not predict the numbers, hence it is more random than any pseudo-random programming function.

This is my very basic setup: solar panel's + on PIN26, - on one of the GND. If you use bigger solar panel protect your board!
![Raspberry Pico with solar panel](https://raw.githubusercontent.com/akosnikhazy/Raspberry-Pico-Projects/main/random-number-generator.JPG)
