import time
import RPi.GPIO as GPIO

gpio_pin = 21
dur = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.OUT)

def toggle_relay(state):
    if state == "on":
        GPIO.output(gpio_pin, GPIO.HIGH)
        print("Relay On")
    elif state == "off":
        GPIO.output(gpio_pin, GPIO.LOW)
        print("Relay Off")
    else:
        print("Invalid argument. Use 'on' or 'off'")

    GPIO.cleanup()
    return