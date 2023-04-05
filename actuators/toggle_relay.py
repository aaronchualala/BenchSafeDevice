import time
import RPi.GPIO as GPIO


def toggle_relay(state):
    gpio_pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    
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