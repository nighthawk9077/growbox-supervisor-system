########
# setup rpi hardware
# Version: V20-01-27 (This is a working BETA vesion)
# Todd Moore
# 1.27.20
#
# This project is released under The MIT License (MIT)
# Copyright 200.59 Todd Moore
########

########
# # Code is compatible with Python 2.7 and Python 3.5.
#!/usr/bin/env python
# coding=utf-8
########

########
# sets up the RPI & GrovePi+ Hat hardware inputs & outputs
########

import time
import grovepi
import config

def hardware():
    
    # setup RPI/GrovePi+ hardware pins
    # --------------Setup Hardware  ---------------------
    grovepi.pinMode(config.BUZZER,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital output
    time.sleep(0.5)
        
    grovepi.pinMode(config.MOISTURE_SENSOR2,"INPUT") # Connect the 2nd Grove Moisture Sensor to analog input
    time.sleep(0.5)
    
    grovepi.pinMode(config.MOISTURE_SENSOR,"INPUT") # Connect the Grove Moisture Sensor to analog input
    time.sleep(0.5)

    grovepi.pinMode(config.TEMP_SENSOR,"INPUT") # Connect the Grove Temp/Humid Sensor to digital input
    time.sleep(0.5)

    grovepi.pinMode(config.ATOMIZER,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital output
    time.sleep(0.5)

    grovepi.pinMode(config.LIGHT,"OUTPUT") # Connect the Grove 2 ch relay (top relay) to digital output
    time.sleep(0.5)
    
    grovepi.pinMode(config.FAN,"OUTPUT") # Connect the Grove 2 ch relay (bottom relay) to digital output
    time.sleep(0.5)
    
    grovepi.pinMode(config.TEMP_ALARM_LED,"OUTPUT")  # Connect Temperature Alarm LED to digital output
    time.sleep(0.5)      
        
    grovepi.pinMode(config.HUMID_ALARM_LED,"OUTPUT") # Connect Humidity Alarm LED to digital output
    time.sleep(0.5)
        
    grovepi.pinMode(config.MOISTURE_ALARM_LED,"OUTPUT") # Connect Moisture Alarm LED to digital output
    time.sleep(0.5)

    grovepi.pinMode(config.ATOMIZER_ON_LED,"OUTPUT") # Connect Atomizer ON LED to digital output
    time.sleep(0.5)

    grovepi.pinMode(config.MOISTURE2_ALARM_LED,"OUTPUT")  # Connect Smoke Alarm Buzzer to digital output
    time.sleep(0.5)
    