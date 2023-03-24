import time
import RPi.GPIO as GPIO

gpio_pin = 21
dur = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(gpio_pin, GPIO.LOW)
        print("Relay Off")
        time.sleep(dur)
        GPIO.output(gpio_pin, GPIO.HIGH)

        print("Relay On")
        time.sleep(dur)
finally:
    GPIO.cleanup()