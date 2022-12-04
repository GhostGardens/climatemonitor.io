import os
import time
from datetime import datetime
import socket

import pigpio
import DHT

def get_sensor_readings():
    pin = 4
    epoch = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    sensor = DHT.DHTAUTO
    pi = pigpio.pi()
    if not pi.connected:
        print('No connection to sensor!  Make sure pigpiod is running!')
        exit()

    s = DHT.sensor(pi, pin, model = sensor)

    tries = 5
    while tries:
        try:
            timestamp, gpio, status, celsius, humidity = s.read()
            if(status == DHT.DHT_TIMEOUT): # no response from sensor
                exit()
            if(status == DHT.DHT_GOOD):
                print('Got {} {}'.format(celsius, humidity))
                break
            time.sleep(2)
            tries -=1
        except KeyboardInterrupt:
            exit()

    temperature = (celsius * 9/5) + 32
    result = {
            'asof' : epoch,
            'hostname' : hostname,
            'temperature' : temperature,
            'humidity' : humidity
            }

    return result

if __name__ == '__main__':
    get_sensor_readings()
