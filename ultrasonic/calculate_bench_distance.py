from click import echo
from gpiozero import DistanceSensor
import time
import RPi.GPIO as GPIO

def calculate_bench_distance(echo, trigger):
    for i in range(6):
        distance = ultrasonic(echo, trigger)
        print("distance: " + str(distance) + " cm")
        time.sleep(0.5)
    GPIO.cleanup()
    return distance

def ultrasonic(echo, trigger):
    pinTrigger = trigger
    pinEcho = echo
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)

    GPIO.output(pinTrigger, GPIO.LOW)
    GPIO.output(pinTrigger, GPIO.HIGH)

    time.sleep(0.00001)
    GPIO.output(pinTrigger, GPIO.LOW)
    
    while GPIO.input(pinEcho)==0:
        pulseStartTime = time.time()
    while GPIO.input(pinEcho)==1:
        pulseEndTime = time.time()
    
    pulseDuration = pulseEndTime - pulseStartTime
    distance = round(pulseDuration*17150, 2)
    return distance