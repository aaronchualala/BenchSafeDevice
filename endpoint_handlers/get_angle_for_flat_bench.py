import math

def get_angle_for_flat_bench(
    bench_length, 
    angle_between_bench_and_slope,
    nipple_height,
    vertical_distance_from_bench_to_device
    ):
    
    l = float(nipple_height) + (vertical_distance_from_bench_to_device / math.tan( angle_between_bench_and_slope ))

    ll = bench_length - l
    
    angle = math.atan( ll / vertical_distance_from_bench_to_device ) * 180 / math.pi
    
    return angle