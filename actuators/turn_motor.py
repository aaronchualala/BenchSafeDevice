import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

def turn_motor(angle):
    GpioPins = [18, 23, 24, 25]
    mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    time.sleep(0.1)
    mymotortest.motor_run(GpioPins,.05,128, True, True,"full", .05)
    GPIO.cleanup()
    return
