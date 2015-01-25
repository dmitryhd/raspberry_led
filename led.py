#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setmode(GPIO.BOARD)

RED_LED = 12
GREEN_LED = 16
delay = 0.1
duration = 20


def power_on(led_num):
    GPIO.setup(led_num, GPIO.OUT)
    GPIO.output(led_num, GPIO.HIGH)


def power_off(led_num):
    GPIO.setup(led_num, GPIO.IN)


def main():
    if len(sys.argv) == 3:
        delay = float(sys.argv[1])
        duration = int(sys.argv[2])
        it_num = int(duration / delay)
        
    for i in range(it_num):
        power_on(RED_LED)
        power_off(GREEN_LED)
        print('Red ON')
        sleep(DELAY)
        power_off(RED_LED)
        power_on(GREEN_LED)
        print('Red OFF')
        sleep(DELAY)

    GPIO.cleanup()


if __name__ == '__main__':
    try:
        main()
    except:
        print('Cleaning up.')
        GPIO.cleanup()
        raise
