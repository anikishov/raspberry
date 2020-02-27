#!/opt/me/env/bin/python3

import os, requests
from flask import Flask

app = Flask(__name__)

@app.route('/temp', methods = ['GET'])
def give_temp():
    temp = os.popen('vcgencmd measure_temp').read()

    enviroment = {}

    enviroment['hostname'] = os.uname()[1]
    enviroment['temperature'] = temp.rstrip('\'C\n').split('=')[1] # parse - temp=29.0'C\n

    return enviroment

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

