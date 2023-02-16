from flask import Flask, request
from read_gym_admin_values import read_gym_admin_values
from get_angle_for_flat_bench import get_angle_for_flat_bench
from get_angle_for_inclined_bench import get_angle_for_inclined_bench

GYM_ADMIN_VALUES = read_gym_admin_values()
app = Flask(__name__)



@app.route('/angle-for-flat-bench') 
# http://127.0.0.1:5000/angle-for-flat-bench?nipple_height=1.2
def endpoint_1():

    # ——— data from admin ———
    bench_length = GYM_ADMIN_VALUES['bench_length']
    angle_between_flat_bench_and_slope = GYM_ADMIN_VALUES['angle_between_flat_bench_and_slope']
    # ——— data from user ———
    nipple_height = request.args.get('nipple_height')
    # ——— data from GPIO ———
    vertical_distance_from_flat_bench_to_device = 2

    return str(
        get_angle_for_flat_bench(
            bench_length, 
            angle_between_flat_bench_and_slope,
            nipple_height,
            vertical_distance_from_flat_bench_to_device
        ))



@app.route('/angle-for-inclined-bench')
# http://127.0.0.1:5000/angle-for-inclined-bench?nipple_height=1.2
def endpoint_2():

    # ——— data from admin ———
    bench_length = GYM_ADMIN_VALUES['bench_length']
    angle_between_flat_bench_and_slope = GYM_ADMIN_VALUES['angle_between_flat_bench_and_slope']
    # ——— data from user ———
    nipple_height = request.args.get('nipple_height')
    # ——— data from GPIO ———
    vertical_distance_from_flat_bench_to_device = 2
    vertical_distance_from_inclined_bench_to_device = 1.5 # diff
    angle_between_flat_bench_and_inclined_bench = 30 # diff

    return str(
        get_angle_for_inclined_bench(
            bench_length, 
            angle_between_flat_bench_and_slope,
            nipple_height,
            vertical_distance_from_flat_bench_to_device,
            vertical_distance_from_inclined_bench_to_device, # diff
            angle_between_flat_bench_and_inclined_bench # diff
        ))



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')