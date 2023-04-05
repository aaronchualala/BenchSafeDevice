import math

def get_angle_for_inclined_bench(
    bench_length, 
    angle_between_flat_bench_and_slope,
    nipple_height,
    vertical_distance_from_flat_bench_to_device,
    vertical_distance_from_inclined_bench_to_device, # diff
    angle_between_flat_bench_and_inclined_bench # diff
    ):

    x = 0.3
    
    #horizontal distance from device to bar
    B = bench_length
    theta =  angle_between_flat_bench_and_slope
    y = angle_between_flat_bench_and_inclined_bench
    N = nipple_height
    H = vertical_distance_from_flat_bench_to_device

    l = B*math.cos(y) -  N*math.cos(y) - math.tan(theta)*(H - N*math.sin*(y))
    results = math.atan((H - B* math.sin(y))/(x+l))

    return results

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

    