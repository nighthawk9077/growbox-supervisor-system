# Get air quality from Grove sensor MQ2 connected to GrovePi+ port A1
# Code taken from: http://wiki.seeedstudio.com/Grove-Gas_Sensor-MQ2/

import time
import grovepi

# Connect the Grove Gas Sensor to analog port A1
# SIG,NC,VCC,GND
gas_sensor = 1

grovepi.pinMode(gas_sensor,"INPUT")

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(gas_sensor)

        # Calculate gas density - large value means more dense gas
        density = (float)(sensor_value / 1024.0)

        print("sensor_value =", sensor_value, " density =", density)
        time.sleep(.5)

    except IOError:
        print ("Error")
