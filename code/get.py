########
# get values from sensors
# Version: V20-01-27 (This is a working BETA vesion)
# Todd Moore
# 1.27.20
#
# This project is released under The MIT License (MIT)
# Copyright 2020 Todd Moore
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
import bme280
import config

def dht22_values():
    try:
        # Get DHT22 Temperature & Humidity
        # The first parameter is the port, the second parameter is the type of sensor.
        [config.tempF, config.humidity] = grovepi.dht(config.TEMP_SENSOR,config.WHITE) 
        # Convert to Fahrenheit = 9.0/5.0 * Celsius + 32
        config.tempF = (9/5 * config.tempF) + 32

        # calibrate the temp
        # config.tempF = config.tempF * 1.6279 - 15.833
        # config.tempF = ((config.tempF**2 * 0.0336) - (1.7846 * config.tempF) + 69.078)
        config.tempF = round(((config.tempF**2 * 0.034) - (1.78 * config.tempF) + 69.08) - 6.0, 1)

        # calibrate the humidity
        # config.humidity = (0.4477 * (config.humidity**1.0516)) 
        config.humidity = ((0.6007 * config.humidity) - 2.9439) 
        config.humidity = round(config.humidity, 1)
    except IOError:
        print ("DHT22 Temp/Humid Sensor Error")

    if(config.DEBUG):
        print("Temp/Humidity is: ", config.tempF, config.humidity)
        print("get.dht22_values module done")
    time.sleep(1)

def bme280_values():
    try:
        # Get BME280 Temperature, Humidity, & Pressure
        (config.bme280_chip_id, config.bme280_chip_version) = bme280.readBME280ID()
        config.bme280_temperature, config.bme280_pressure, config.bme280_humidity = bme280.readBME280All()
        # Convert to Fahrenheit = 9.0/5.0 * Celsius + 32
        config.bme280_tempF = ((9/5 * config.bme280_temperature) + 32.00)
        # temp calibration equation
        # config.bme280_tempF = ((0.646 * config.bme280_tempF) + (33.0))
        # config.bme280_tempF = ((0.646 * config.bme280_tempF) + (33.786))
        config.bme280_tempF = 1.5107*(config.bme280_tempF) - 14.541

        config.bme280_tempF = round(config.bme280_tempF, 1)
        
        # humid calibration equation
        config.bme280_humidity = (0.8223 * config.bme280_humidity + 15.386)
        config.bme280_humidity = round(config.bme280_humidity, 1)
        config.bme280_pressure = round(config.bme280_pressure/33.864, 1)
    except IOError:
        print ("BME280 Temp/Humid/Pressure Sensor Error")

    if(config.DEBUG):
        print("BME280 Temp/Humidity/Pressure is: ", config.bme280_tempF, config.bme280_humidity,config.bme280_pressure)
        print("get.bme280_values module done")
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
    except IOError:
        print ("Moisture Sensor Error")

    try:
        config.moisture2 = grovepi.analogRead(config.MOISTURE_SENSOR2)
    except IOError:
        print ("Moisture2 Sensor Error")

    if(config.DEBUG):
        print("Soil Moisture/Soil Moisture2 is: ", config.moisture, config.moisture2)
        print("get.moisture module done")
    time.sleep(1)
            
# run main() function
if __name__ == "__main__":
    # -------- Test Vectors ------------
    config.DEBUG = True
    dht22_values()
    bme280_values()
    moisture()  
