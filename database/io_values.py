import os, json

def read_gym_admin_values():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './gym_admin_values.json')
    gym_admin_values =  json.load(open(data_file))
    print('read gym_admin_values: ', gym_admin_values)
    return gym_admin_values

def write_gym_admin_values(gym_admin_values):
    print("write gym_admin_values: ", gym_admin_values)
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './gym_admin_values.json')
    with open(data_file, 'w') as outfile:
        json.dump(gym_admin_values, outfile)
    return 

def read_device_state_values():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './device_state_values.json')
    device_state_values =  json.load(open(data_file))
    print('read device_state_values: ', device_state_values)
    return device_state_values

def write_device_state_values(device_state_values):
    print("write device_state_values: ", device_state_values)
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './device_state_values.json')
    with open(data_file, 'w') as outfile:
        json.dump(device_state_values, outfile)
    return 


if __name__ == '__main__':
    read_gym_admin_values()
    write_gym_admin_values(
        {
            "bench_length": 0.90,
            "angle_between_flat_bench_and_slope": 81
        }
    )
    read_device_state_values()
    write_device_state_values(
        {
            "steps_from_vertical_in_ccwise_direction": 0
        }
    )
    read_device_state_values()