import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
time.sleep(2)
GPIO.output(2, GPIO.HIGH)
time.sleep(2)
GPIO.output(2, GPIO.LOW)

GPIO.cleanup()