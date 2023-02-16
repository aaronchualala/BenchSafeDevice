import os, json

def read_gym_admin_values():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, './gym_admin_values.json')
    gym_admin_values =  json.load(open(data_file))

    return gym_admin_values
