from time import sleep
from flask import Flask, request
from flask_cors import CORS
import gyroscope

app = Flask(__name__)
cors = CORS(app)
app.config['COR_HEADERS'] = 'Content-Type'

@app.route('/get_angle_between_flat_bench_and_inclined_bench')
def endpoint_1():
    angle = 0
    for i in range(10):
        angle = gyroscope.get_angle_between_flat_bench_and_inclined_bench()
        print(angle)
        sleep(1)
    return angle

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')