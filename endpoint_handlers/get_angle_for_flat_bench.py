import math

def get_angle_for_flat_bench(
    bench_length, 
    angle_between_bench_and_slope,
    nipple_height,
    vertical_distance_from_bench_to_device
    ):
    in_rad = (angle_between_bench_and_slope / 180 )* math.pi

    #horizontal distance from device to bar
    x = 0.3

    B = float(bench_length)
    theta =  float(in_rad)
    N = float(nipple_height)
    H = float(vertical_distance_from_bench_to_device)

    # H_over_tan_theta = (vertical_distance_from_bench_to_device / math.tan( in_rad ))
    # l = float(nipple_height) + H_over_tan_theta

    # if bench_length - l < 0:
    #     return "ERROR"
    # else:
    #     ll = bench_length - l
    
    # angle = math.atan( ll / vertical_distance_from_bench_to_device ) * 180 / math.pi

    y = B - H* (math.tan(theta)) - N
    print("y")
    print(y)
    angle = math.atan((x+y)/H)* 180 / math.pi

    print("angle in get_angle: ", angle)

    return angle

if __name__ == "__main__":
    print(get_angle_for_flat_bench(2, 80, 1.4, 0.001))
    print('\n')
    print(get_angle_for_flat_bench(2, 80, 1.4, 2.5))
    print('\n')
    print(get_angle_for_flat_bench(2, 80, 1.4, 10))