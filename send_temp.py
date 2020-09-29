#!/opt/me/env/bin/python3

import os, requests
from flask import Flask,request

app = Flask(__name__)

'''
This route and function will set wireguard interface
'''
def set_gw(iface):
    result = os.popen(f'systemctl start wg-quick@{iface}').read()
    return result

def get_gw():
    result = os.popen('wg').read()
    return result

@app.route('/gw', methods = ['POST','GET'])
def gw():
    if request.method == 'POST':
        data = request.get_json(force=True)
        if data['iface']:
            iface = data['iface']
            result = set_gw(iface)
            return result, 200
        else:
            return data, 400
    elif request.method == 'GET':
        return get_gw()

@app.route('/temp', methods = ['GET'])
def give_temp():
    temp = os.popen('vcgencmd measure_temp').read()

    enviroment = {}

    enviroment['hostname'] = os.uname()[1]
    enviroment['temperature'] = temp.rstrip('\'C\n').split('=')[1] # parse - temp=29.0'C\n

    return enviroment

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

