import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib


def turn_motor(number_of_steps, is_ccwise):
    my_motor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")
    
    my_motor.motor_run(
        gpiopins=[18, 23, 24, 25], 
        wait=.001, 
        steps=number_of_steps, 
        ccwise=is_ccwise, 
        verbose=False, 
        steptype="half", 
        initdelay=0.05
    )

    GPIO.cleanup()
    return
