########
# determines if value is the highest or lowest
# Version: 2019-03-27V1A (This is an alpha version & not yet complete
# Todd Moore
# 3.27.19
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
# returns high & low values of temp, humidity, moisture, & density
########

import config

def hi_lo_temp():
    # hi temperature value
    if config.tempF > config.hi_temp_value:
        config.hi_temp_value = config.tempF
    # low temperature value
    if config.tempF < config.lo_temp_value:
        config.lo_temp_value = config.tempF
    if(config.DEBUG):
        print ("Hi Temp ", config.hi_temp_value, "Lo Temp ", config.lo_temp_value)

def hi_lo_humid():
   # hi humidity value
    if config.humidity > config.hi_humid_value:
        config.hi_humid_value = config.humidity
    # low humidity value
    if config.humidity < config.lo_humid_value:
        config.lo_humid_value = config.humidity
    if(config.DEBUG):
        print("Hi Humid ", config.hi_humid_value, "Lo Humid ", config.lo_humid_value)
        
def hi_lo_moisture():
    # hi moisture value
    if config.moisture > config.hi_moisture_value:
        config.hi_moisture_value = config.moisture
    # low moisture value
    if config.moisture < config.lo_moisture_value:
        config.lo_moisture_value = config.moisture
    if(config.DEBUG):
        print("Hi Moisture ", config.hi_moisture_value, "Lo Moisture ", config.lo_moisture_value)

def hi_lo_density():
     # hi density value
    if config.density > config.hi_density_value:
        config.hi_density_value = config.density
    # low moisture value
    if config.density < config.lo_density_value:
        config.lo_density_value = config.density
    if(config.DEBUG):
        print("Hi Density ", config.hi_density_value, "Lo Density ", config.lo_density_value)
 
 
# run main() function
if __name__ == "__main__":
    config.DEBUG = True 
    hi_lo_temp()
    hi_lo_humid()
    hi_lo_moisture()
    hi_lo_density()

    # Set the low values
    tempF = 55.0
    humidity = 55.0
    moisture = 200
    density = 600
    
    hi_lo_temp()
    hi_lo_humid()
    hi_lo_moisture()
    hi_lo_density()
