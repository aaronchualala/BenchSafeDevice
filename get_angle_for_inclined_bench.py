import math

def get_angle_for_inclined_bench(
    bench_length, 
    angle_between_flat_bench_and_slope,
    nipple_height,
    vertical_distance_from_flat_bench_to_device,
    vertical_distance_from_inclined_bench_to_device, # diff
    angle_between_flat_bench_and_inclined_bench # diff
    ):

    L = ( vertical_distance_from_flat_bench_to_device - vertical_distance_from_inclined_bench_to_device) / math.tan(angle_between_flat_bench_and_inclined_bench)

    numerator = l = (
        bench_length * math.cos(angle_between_flat_bench_and_inclined_bench)
        - (
            ( vertical_distance_from_flat_bench_to_device - vertical_distance_from_inclined_bench_to_device )
            / math.tan(angle_between_flat_bench_and_inclined_bench)
        )
    )
    
    denominator = (
        vertical_distance_from_inclined_bench_to_device
        - (
            math.sqrt(
                (
                    bench_length - (L / math.cos(angle_between_flat_bench_and_inclined_bench))
                )**2
                - l**2
            )
        )
    )

    before_atan = numerator / denominator 

    results = math.atan( before_atan ) * 180 / math.pi

    return results