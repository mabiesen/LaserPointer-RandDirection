import RPi.GPIO as GPIO
import time
import random

while True:
#This is the first servo
    spam=random.randint(6,9) #altering the figures in randint will alter range of pointer
    target = random.randint(1,2) #target assigned to allow the possibility of non-integer ingcrements, increasing randomness
    if target ==2:
        spam = spam
    GPIO.setmode(GPIO.BOARD) #declare the reference style for GPIO
    GPIO.setup(23,GPIO.OUT) #assign pin 23 as an output
    pwm=GPIO.PWM(23,50) #sets PWM for the pin
    pwm.start(5)
    pwm.ChangeDutyCycle(spam) #moves pointer to location designated by spam
    time.sleep(1) #slows down operations, toggle argument to toggle time spent doing nothing
    GPIO.cleanup() #clears the GPIO. 

#This is the second servo
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
