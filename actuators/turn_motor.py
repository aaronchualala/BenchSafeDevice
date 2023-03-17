import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

def turn_motor(steps):
    direction = True if steps > 0 else False
    GpioPins = [18, 23, 24, 25]
    my_motor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")
    time.sleep(0.1)
    my_motor.motor_run(
        gpiopins=GpioPins, 
        wait=.001, 
        steps=abs(steps), 
        ccwise=direction, 
        verbose=False, 
        steptype="half", 
        initdelay=0.05)
    GPIO.cleanup()
    return
