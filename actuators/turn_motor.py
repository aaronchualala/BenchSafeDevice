import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

def turn_motor(angle):
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    return