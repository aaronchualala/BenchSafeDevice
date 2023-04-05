import os, json

def read_gym_admin_values():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './gym_admin_values.json')
    gym_admin_values =  json.load(open(data_file))
    return gym_admin_values

def write_gym_admin_values(gym_admin_values):
    print("gym_admin_values: ", gym_admin_values)
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './gym_admin_values.json')
    with open(data_file, 'w') as outfile:
        json.dump(gym_admin_values, outfile)
    return 

def read_device_state_values():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './device_state_values.json')
    device_state_values =  json.load(open(data_file))
    return device_state_values

def write_device_state_values(device_state_values):
    print("device_state_values: ", device_state_values)
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './device_state_values.json')
    with open(data_file, 'w') as outfile:
        json.dump(device_state_values, outfile)
    return 