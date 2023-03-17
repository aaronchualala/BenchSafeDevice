from click import echo
from gpiozero import DistanceSensor
import time
ultrasonic = DistanceSensor(echo=17, trigger=4)

def calculate_bench_distance():
    while True:
        print(ultrasonic.distance)
        time.sleep(1)