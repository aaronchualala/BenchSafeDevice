# https://pypi.org/project/mpu6050-raspberrypi/
# https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi#:~:text=The%20MPU6050%20sensor%20module%20is,using%20its%20Auxiliary%20I2C%20bus
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

def get_angle_between_flat_bench_and_inclined_bench():
    accelerometer_data = sensor.get_accel_data()
    # gyro_data = sensor.get_gyro_data()
    # temp = sensor.get_temp()
    print("accelerometer_data: ", accelerometer_data)
    # print("gyro_data: ", gyro_data)
    # print("temp: ", temp)
    return 30