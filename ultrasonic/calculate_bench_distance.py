from click import echo
from gpiozero import DistanceSensor
import time
ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance = 300)

def calculate_bench_distance():
    while True:
        print(f"{ultrasonic.distance*300} cm")
        time.sleep(1)