from flask import Flask, request
from flask_cors import CORS
from database import io_values
from endpoint_handlers import get_angle_for_flat_bench
from endpoint_handlers import get_angle_for_inclined_bench
from actuators import turn_motor
from actuators import toggle_relay
from ultrasonic import calculate_bench_distance
import requests

GYM_ADMIN_VALUES = io_values.read_gym_admin_values()
DEVICE_STATE_VALUES = io_values.read_device_state_values()
app = Flask(__name__)
cors = CORS(app)
app.config['COR_HEADERS'] = 'Content-Type'

@app.route('/angle-for-flat-bench') 
# http://127.0.0.1:5000/angle-for-flat-bench?nipple_height=0.37
def endpoint_1():

    # ——— data from admin ———
    bench_length = float(GYM_ADMIN_VALUES['bench_length'])
    angle_between_flat_bench_and_slope = float(GYM_ADMIN_VALUES['angle_between_flat_bench_and_slope'])
    # ——— data from user ———
    nipple_height = float(request.args.get('nipple_height'))
    print('nipple_height: ', nipple_height)
    # ——— data from GPIO ———
    vertical_distance_from_flat_bench_to_device = calculate_bench_distance.calculate_bench_distance(17,4)
    if vertical_distance_from_flat_bench_to_device == 0.0:
        return str("ERROR: 'vertical_distance_from_flat_bench_to_device' cannot be 0.0")
    print('vertical_distance_from_flat_bench_to_device: ', vertical_distance_from_flat_bench_to_device)

    # calculations
    angle = get_angle_for_flat_bench.get_angle_for_flat_bench(
        bench_length, 
        angle_between_flat_bench_and_slope,
        nipple_height,
        vertical_distance_from_flat_bench_to_device
    )
    print('angle: ', angle)
    steps_to_revert = DEVICE_STATE_VALUES['steps_from_vertical_in_ccwise_direction']
    steps_to_new_pos = abs(int(angle / 0.703125)) # angle_change_for_each_step
    print('steps_to_revert: ', steps_to_revert)
    print('steps_to_new_pos: ', steps_to_new_pos)

    # storage
    DEVICE_STATE_VALUES['steps_from_vertical_in_ccwise_direction'] = steps_to_new_pos
    io_values.write_device_state_values(DEVICE_STATE_VALUES)
    
    # actuation
    turn_motor.turn_motor(steps_to_revert, is_ccwise=False)
    turn_motor.turn_motor(steps_to_new_pos, is_ccwise=True)

    toggle_relay.toggle_relay("on")

    return "OK, Motor should be turning"

@app.route('/angle-for-inclined-bench')
# http://127.0.0.1:5000/angle-for-inclined-bench?nipple_height=0.37&angle=30
def endpoint_2():

    # ——— data from admin ———
    bench_length = float(GYM_ADMIN_VALUES['bench_length'])
    angle_between_flat_bench_and_slope = float(GYM_ADMIN_VALUES['angle_between_flat_bench_and_slope'])
    # ——— data from user ———
    nipple_height = float(request.args.get('nipple_height'))
    print('nipple_height: ', nipple_height)
    # ——— data from GPIO ———
    vertical_distance_from_flat_bench_to_device = 1.20 
    vertical_distance_from_flat_bench_to_device = calculate_bench_distance.calculate_bench_distance(17,4)
    if vertical_distance_from_flat_bench_to_device == 0.0:
        return str("ERROR: 'vertical_distance_from_flat_bench_to_device' cannot be 0.0")
    print('vertical_distance_from_flat_bench_to_device: ', vertical_distance_from_flat_bench_to_device)

    angle_between_flat_bench_and_inclined_bench = float(request.args.get('angle')) if request.args.get('angle') is not None else 30.0
    # angle_between_flat_bench_and_inclined_bench = requests.get('http://172.20.10.12:5000/get_angle_between_flat_bench_and_inclined_bench')

    angle = get_angle_for_inclined_bench.get_angle_for_inclined_bench(
        bench_length, 
        angle_between_flat_bench_and_slope,
        nipple_height,
        vertical_distance_from_flat_bench_to_device,
        angle_between_flat_bench_and_inclined_bench # diff
    )
    print('angle: ', angle)
    steps_to_revert = DEVICE_STATE_VALUES['steps_from_vertical_in_ccwise_direction']
    steps_to_new_pos = abs(int(angle / 0.703125)) # angle_change_for_each_step
    print('steps_to_revert: ', steps_to_revert)
    print('steps_to_new_pos: ', steps_to_new_pos)

    # storage
    DEVICE_STATE_VALUES['steps_from_vertical_in_ccwise_direction'] = steps_to_new_pos
    io_values.write_device_state_values(DEVICE_STATE_VALUES)
    
    # actuation
    turn_motor.turn_motor(steps_to_revert, is_ccwise=False)
    turn_motor.turn_motor(steps_to_new_pos, is_ccwise=True)

    toggle_relay.toggle_relay("on")

    return "OK, Motor should be turning"

@app.route('/toggle-relay')
# http://127.0.0.1:5000/toggle-relay?state=on
# http://127.0.0.1:5000/toggle-relay?state=off
def endpoint_3():
    state = request.args.get('state')
    toggle_relay.toggle_relay(state)
    return "OK, Should have turned " + state

@app.route('/update-json')
def endpoint_4():
    # request.json: parsed JSON data. The request must have the application/json content type
    bench_length = request.args.get('bench_length')
    angle_between_flat_bench_and_slope = request.args.get('angle_between_flat_bench_and_slope')
    print(request.args)
    io_values.write_gym_admin_values({
        'bench_length': bench_length,
        'angle_between_flat_bench_and_slope': angle_between_flat_bench_and_slope
    })
    return "OK, Should have updated JSON"

@app.route('/calibrate-motor')
# http://127.0.0.1:5000/calibrate-motor?number_of_steps=5&is_ccwise=True
def endpoint_5():
    number_of_steps = request.args.get('number_of_steps')
    is_ccwise = False if request.args.get('is_ccwise') == "False" else True
    turn_motor.calibrate_motor(int(number_of_steps), bool(is_ccwise))
    return "OK, Motor should be turning"

@app.route('/ping')
def endpoint_6():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
