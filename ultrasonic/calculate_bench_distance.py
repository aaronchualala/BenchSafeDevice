from click import echo
from gpiozero import DistanceSensor
import time

ultrasonic = DistanceSensor(echo=17, trigger=4)

def calculate_bench_distance():
    for i in range(6):
        print("ultrasonic distance: ", ultrasonic.distance)
        time.sleep(0.5)
    return ultrasonic.distance