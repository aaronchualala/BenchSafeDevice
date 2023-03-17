from click import echo
from gpiozero import DistanceSensor
import time
import RPi.GPIO as GPIO

def calculate_bench_distance():
    count = 6
    while count != 0:
        print( str(ultrasonic.distance*300) + " cm")
        time.sleep(0.5)
        count -=1
    
#     return ultrasonic.distance*300


def ultrasonic_dist(echo=17, trigger=4):
    GPIO.setmode(GPIO.BOARD)
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
    print(f'distance: {distance} cm')
    
    return distance