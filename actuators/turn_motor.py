import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

def turn_motor(angle):
    GpioPins = [18, 23, 24, 25]
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    mymotortest.motor_run(GpioPins , .01, 100, False, False, "half", .05)
    return