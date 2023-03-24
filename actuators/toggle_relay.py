import time
import RPi.GPIO as GPIO


def toggle_relay(state):
    if state == "on":
        try:
            gpio_pin = 21
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(gpio_pin, GPIO.OUT)
            GPIO.output(gpio_pin, GPIO.HIGH)
            print("Relay On")
        except:
            print("Relay is already on")
    elif state == "off":
        try:
            GPIO.output(gpio_pin, GPIO.LOW)
            print("Relay Off")
            GPIO.cleanup()
        except:
            print("Relay is already off")
    else:
        print("Invalid argument. Use 'on' or 'off'")

    return