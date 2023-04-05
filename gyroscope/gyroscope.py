# https://pypi.org/project/mpu6050-raspberrypi/
# https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi#:~:text=The%20MPU6050%20sensor%20module%20is,using%20its%20Auxiliary%20I2C%20bus
from mpu6050 import mpu6050
import math

sensor = mpu6050(0x68)

def get_angle_between_flat_bench_and_inclined_bench():
    accelerometer_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()

    ax = accelerometer_data['x']
    ay = accelerometer_data['y']
    az = accelerometer_data['z']

    roll = math.atan2(ay, math.sqrt(ax * ax + az * az)) * 180 / math.pi
    pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az)) * 180 / math.pi

    print("accelerometer_data: ", accelerometer_data)
    print("gyro_data: ", gyro_data)
    print("Roll: ", roll)
    print("Pitch: ", pitch)

    # You can return either roll or pitch depending on the angle you want to measure
    # relative to the horizontal plane
    return abs(roll) #, pitch
