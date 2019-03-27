# Get soil moisture from Grove moisture sensor connected to the GrovePi+ Hat
# http://wiki.seeedstudio.com/Grove-Moisture_Sensor/

# Sensor is connected to A2 of the GrovePi+ Hat

#   Here are suggested sensor values:
#       Min  Typ  Max  Condition
#       0    0    0    sensor in open air
#       0    20   300  sensor in dry soil
#       300  580  700  sensor in humid soil
#       700  940  950  sensor in water


import time
import grovepi

# Connect the Grove Moisture Sensor to analog port A2
# SIG,NC,VCC,GND
sensor = 2

while True:
    try:
        moisture = grovepi.analogRead(sensor)
        print(moisture)
        time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
