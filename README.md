# LaserPointerRandDir-Python
Code for laser pointer dog toy that I built using two servos to create a turret:

1. The first servo spins on a vertical axis and is locked in place to a baseboard and drives the top of a swivel(the bottom of which is also locked in place by the baseboard). This will provide side to side movement.
2.  The second servo is on top of the swivel and spins on a horizontal axis. This servo has an arm connected to a laser pointer.  This servo drives the up and down movement.

Two variables are utilized to control servo direction: spam and target.  The reason for these two variables
 is to control both the integer and float independently such that servos may run on a pwm duty cycle in random, 0.5 increments.

There are many improvements available to this code.  For example, it is not necessary to clear the GPIO on every iteration of the while loop.  But the code works as is and is an example for RPi beginners.
