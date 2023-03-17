from click import echo
from gpiozero import DistanceSensor
import time
ultrasonic = DistanceSensor(echo=17, trigger=4)

def calculate_bench_distance():
    print("ultrasonic.distance")
    print(ultrasonic.distance)
    print("WOOHOO")
    time.sleep(1)
    return