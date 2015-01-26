#!/usr/bin/env python2

from flask import Flask, request, render_template

#from led import *
RED_LED = 0
GREEN_LED = 1
def power_on(led_num):
    print('execute power on', led_num)

def power_off(led_num):
    print('execute power off', led_num)

app = Flask(__name__)

@app.route('/')
def led_control():
    red_state = request.args.get('red')
    green_state = request.args.get('green')
    if red_state:
        if red_state == 'on':
            print('red on')
            power_on(RED_LED) 
        else:
            print('red off')
            power_off(RED_LED) 
    if green_state:
        if green_state == 'on':
            print('green on')
            power_on(GREEN_LED) 
        else:
            print('green off')
            power_off(GREEN_LED) 
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
