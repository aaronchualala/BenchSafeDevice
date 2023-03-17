from flask import Flask, request
from database import io_values
from endpoint_handlers import get_angle_for_flat_bench
from endpoint_handlers import get_angle_for_inclined_bench
from actuators import turn_motor
from ultrasonic import calculate_bench_distance

GYM_ADMIN_VALUES = io_values.read_gym_admin_values()
DEVICE_STATE_VALUES = io_values.read_device_state_values()
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
    vertical_distance_from_flat_bench_to_device = calculate_bench_distance.calculate_bench_distance()

    if vertical_distance_from_flat_bench_to_device == 0.0:
        return str("ERROR: 'vertical_distance_from_flat_bench_to_device' cannot be 0.0")

    # calculations
    angle = get_angle_for_flat_bench.get_angle_for_flat_bench(
        bench_length, 
        angle_between_flat_bench_and_slope,
        nipple_height,
        vertical_distance_from_flat_bench_to_device
    )

    # storage
    steps_to_revert = DEVICE_STATE_VALUES['steps_from_vertical_in_ccwise_direction']
    steps_to_new_pos = angle / 0.703125 # angle_change_for_each_step
    DEVICE_STATE_VALUES['steps_from_vertical_in_ccwise_direction'] = steps_to_new_pos
    io_values.write_device_state_values(DEVICE_STATE_VALUES)
    
    # actuation
    turn_motor.turn_motor(steps_to_revert, is_ccwise=False)
    turn_motor.turn_motor(steps_to_new_pos, is_ccwise=True)

    # results
    screen_output = "number_of_steps: " + str(number_of_steps) + "\n\n " + "is_ccwise: " + str(is_ccwise)

    return screen_output

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
        get_angle_for_inclined_bench.get_angle_for_inclined_bench(
            bench_length, 
            angle_between_flat_bench_and_slope,
            nipple_height,
            vertical_distance_from_flat_bench_to_device,
            vertical_distance_from_inclined_bench_to_device, # diff
            angle_between_flat_bench_and_inclined_bench # diff
        ))



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')