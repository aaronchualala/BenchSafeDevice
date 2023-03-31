# https://pypi.org/project/mpu6050-raspberrypi/
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

def get_angle_between_flat_bench_and_inclined_bench():
    accelerometer_data = sensor.get_accel_data()
    print(accelerometer_data)
    return 30