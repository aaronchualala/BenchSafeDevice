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
        steptype="half", # has 512 steps for 360 degrees
        initdelay=0.05
    )

    gpio_pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.HIGH)

    GPIO.cleanup()
    return


def calibrate_motor(number_of_steps=5, is_ccwise=True):
    my_motor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")
    
    my_motor.motor_run(
        gpiopins=[18, 23, 24, 25], 
        wait=.001, 
        steps=number_of_steps, 
        ccwise=is_ccwise, 
        verbose=False, 
        steptype="half", # has 512 steps for 360 degrees
        initdelay=0.05
    )

    GPIO.cleanup()
    return
