import math

def get_angle_for_inclined_bench(
    bench_length, 
    angle_between_bench_and_slope,
    nipple_height,
    vertical_distance_from_flat_bench_to_device,
    angle_between_flat_bench_and_inclined_bench # diff
    ):

    print("bench incline angle: ", angle_between_flat_bench_and_inclined_bench)
    in_rad = (angle_between_bench_and_slope / 180 )* math.pi
    in_rad_2 = (angle_between_flat_bench_and_inclined_bench / 180 )* math.pi

    x = 0.3
    
    #horizontal distance from device to bar
    B = float(bench_length)
    theta =  float(in_rad)
    y = float(in_rad_2)
    N = float(nipple_height)
    H = float(vertical_distance_from_flat_bench_to_device)

    l = B*math.cos(y) -  N*math.cos(y) - (math.tan(theta))*(H - N*math.sin(y))
    print("before l: ", B*math.cos(y) -  N*math.cos(y))
    print("l: ", l)
    angle = math.atan((H - B* math.sin(y))/(x+l)) * 180 / math.pi

    print("angle in get_angle: ", angle)

    return angle

    # L = ( vertical_distance_from_flat_bench_to_device - vertical_distance_from_inclined_bench_to_device) / math.tan(angle_between_flat_bench_and_inclined_bench)

    # numerator = l = (
    #     bench_length * math.cos(angle_between_flat_bench_and_inclined_bench)
    #     - (
    #         ( vertical_distance_from_flat_bench_to_device - vertical_distance_from_inclined_bench_to_device )
    #         / math.tan(angle_between_flat_bench_and_inclined_bench)
    #     )
    # )
    
    # denominator = (
    #     vertical_distance_from_inclined_bench_to_device
    #     - (
    #         math.sqrt(
    #             (
    #                 bench_length - (L / math.cos(angle_between_flat_bench_and_inclined_bench))
    #             )**2
    #             - l**2
    #         )
    #     )
    # )

    # before_atan = numerator / denominator 

    # results = math.atan( before_atan ) * 180 / math.pi

    