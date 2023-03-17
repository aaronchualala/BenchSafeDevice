from click import echo
from gpiozero import DistanceSensor
import time
ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance = 300)

def calculate_bench_distance():
    count = 6
    while count != 0:
        print( str(ultrasonic.distance*300) + " cm")
        time.sleep(0.5)
        count -=1
    
    return ultrasonic.distance*300
