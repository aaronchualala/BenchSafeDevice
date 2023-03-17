import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib


def turn_motor(steps):
    # GpioPins = [18, 23, 24, 25]
    # mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")
    # mymotortest.motor_run(GpioPins , .01, 100, False, True, "half", .05)
    print('steps', steps)
    direction = True if steps > 0 else False
    GpioPins = [18, 23, 24, 25]
    my_motor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")
    time.sleep(0.1)

    print("HELP")
    my_motor.motor_run(
        gpiopins=GpioPins, 
        wait=.001, 
        steps=512, #abs(steps), 
        ccwise=False, # direction, 
        verbose=False, 
        steptype="half", 
        initdelay=0.05)
    GPIO.cleanup()
    return
