########
# get values from sensors
# Version: V19-05-20-V1B (This is a working BETA vesion)
# Todd Moore
# 5.20.19
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# # Code is compatible with Python 2.7 and Python 3.5.
#!/usr/bin/env python
# coding=utf-8
########

########
# code that gets values from grove sensors
########

import time
import grovepi
import config

def temp():
    try:
        # Get Temperature & Humidity
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp, humidity] = grovepi.dht(config.TEMP_SENSOR,config.WHITE) 
        # Convert to Fahrenheit = 9.0/5.0 * Celsius + 32
        config.tempF = (9/5 * temp) + 32 + config.temp_calib
        config.humidity = humidity - config.humidity_calib
        if(config.DEBUG):
            print("Temp/Humidity is: ", config.tempF, config.humidity)
            print("get.temp module done")

    except IOError:
        print ("Temp/Humid Sensor Error")
    time.sleep(1)

def moisture():
    #       Min  Typ  Max  Condition
    #       0    0    0    sensor in open air
    #       0    20   300  sensor in dry soil
    #       300  580  700  sensor in humid soil
    #       700  940  950  sensor in water

    #   Sensor values observer: 
    #       Values  Condition
    #       --------------------------
    #       0-17    sensor in open air
    #       18-424  sensor in dry soil
    #       425-689 sensor in humid soil
    #       690+    sensor in water
    try:
        config.moisture = grovepi.analogRead(config.MOISTURE_SENSOR)
        if(config.DEBUG):
            print("get.moisture module done")

    except IOError:
        print ("Moisture Sensor Error")
    time.sleep(1)
            
def air():
    # MQ2 - Combustible Gas, Smoke
    # The sensitivity can be adjusted by the onboard potentiometer
    try:
        # Get Air Quality Value from MQ2 sensor
        # Get sensor value
        sensor_value = grovepi.analogRead(config.GAS_SENSOR)
        # Calculate gas density - large value means more dense gas
        config.density = round((float)(sensor_value / 1024.0)*100, 2)
        if(config.DEBUG):
            print("sensor_value =", sensor_value, " density =", config.density)
            print("get.density done")
    
    except IOError:
        print ("Moisture Sensor Error")
    time.sleep(1)

# run main() function
if __name__ == "__main__":
    # -------- Test Vectors ------------
    config.DEBUG = True
    temp()
    moisture()  
    air()   
