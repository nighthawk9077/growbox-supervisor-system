# Get Temp & Humidity from Temp & Humidity Sensor Pro (AM2302) using the GrovePi + Hat atttached to the RPI.
# http://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/

# Sensor is attached to Port D2, pin D2 of GrovePi + Hat

import grovepi
import math
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D2
# This code uses the white colored sensor.
# SIG,NC,VCC,GND
sensor = 2  # The Sensor goes on digital port 2.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

# This example uses the white colored sensor.
# The first parameter is the port, the second parameter is the type of sensor.
[temp,humidity] = grovepi.dht(sensor,white)  
    if math.isnan(temp) == False and math.isnan(humidity) == False:
        print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
return temp,humidity
