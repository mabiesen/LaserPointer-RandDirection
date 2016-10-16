# LaserPointerRandDir-Python
Code for laser pointer dog toy that I built using two servos.
Two variables are utilized to control servo direction: spam and target.  The reason for these two variables
 is to control both the integer and float independently such that servos may run on a pwm duty cycle in random, 0.5 increments.

```python

import RPi.GPIO as GPIO
import time
import random

while True:
    spam=random.randint(6,9)
    target = random.randint(1,2)
    if target ==2:
        spam = spam
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23,GPIO.OUT)
    pwm=GPIO.PWM(23,50)
    pwm.start(5)
    pwm.ChangeDutyCycle(spam)
    time.sleep(1)
    GPIO.cleanup()

    spam = randint(6,9)
    target = random.randint(1,2)
    if target == 2:
        spam = spam + .5
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32,GPIO.OUT)
    pwm=GPIO.PWM(32,50)
    pwm.start(5)
    pwm.ChangeDutyCycle(spam)
    time.sleep(2)
    GPIO.cleanup()

```
