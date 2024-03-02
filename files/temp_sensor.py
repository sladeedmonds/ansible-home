#!/usr/bin/python

import sys
import datetime
import board
import adafruit_dht

# Log the date and time
timestamp = datetime.datetime.utcnow().isoformat()

# Initialize the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D14)

# Read temperature, convert the temperature to Fahrenheit.
temperature_c = dhtDevice.temperature
temperature_f = temperature_c * (9 / 5) + 32

# Read humidity
humidity = dhtDevice.humidity

# Open log file
f = open('log/temperature-humidity.csv', 'a')

if humidity is not None and temperature_f is not None:
    f.write( str(timestamp) + "," + '{0:0.1f},{1:0.1f}'.format(temperature_f,humidity) + "\n")
else:
    f.write( str(timestamp) + ",fail,fail\n" )

# Close log file and exit
f.close()
sys.exit(1)
