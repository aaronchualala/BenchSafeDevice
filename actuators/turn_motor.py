import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

def turn_motor(angle):
    GpioPins = [17, 18, 27, 22]
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    mymotortest.motor_run(GpioPins , .01, 100, False, False, "half", .05)
    return

while True:
    turn_motor(180)
