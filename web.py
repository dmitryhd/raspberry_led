#!/usr/bin/env python3

from flask import Flask, request, render_template

from led import *

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
    app.run()
