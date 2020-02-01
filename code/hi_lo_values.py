########
# determines if value is the highest or lowest
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
# returns high & low values of temp, humidity, moisture, & density
########

import config

def hi_lo_temp():
    # reset hi & lo temps every day @ midnight
    if (config.light_time == "00:00"):
        config.hi_temp_value = config.tempF
        config.lo_temp_value = config.tempF
    # dht22 hi temperature value
    if config.tempF > config.hi_temp_value:
        config.hi_temp_value = config.tempF
    # bme280 hi temperature value
    if config.bme280_tempF > config.bme280_hi_temp_value:
        config.bme280_hi_temp_value = config.bme280_tempF
        
    # dht22 low temperature value
    if config.tempF < config.lo_temp_value:
        config.lo_temp_value = config.tempF
    # bme280 low temperature value
    if config.bme280_tempF < config.bme280_lo_temp_value:
        config.bme280_lo_temp_value = config.bme280_tempF

    if(config.DEBUG):
        print ("DHT22 Hi Temp ", config.hi_temp_value, "DHT22 Lo Temp ", config.lo_temp_value)
        print ("BME280 Hi Temp ", config.bme280_hi_temp_value, "BME280 Lo Temp ", config.bme280_lo_temp_value)

def hi_lo_humid():
    # reset hi & lo humidity every day @ midnight
    if (config.light_time == "00:00"):
        config.hi_humid_value = config.humidity
        config.lo_humid_value = config.humidity
    # DHT22 hi humidity value
    if config.humidity > config.hi_humid_value:
        config.hi_humid_value = config.humidity
    # BME280 hi humidity value
    if config.bme280_humidity > config.bme280_hi_humid_value:
        config.bme280_hi_humid_value = config.bme280_humidity

    # DHT22 low humidity value
    if config.humidity > config.hi_humid_value:
        config.hi_humid_value = config.humidity
    # BME280 hi humidity value
    if config.bme280_humidity < config.bme280_lo_humid_value:
        config.bme280_lo_humid_value = config.bme280_humidity

    if(config.DEBUG):
        print("DHT22 Hi Humid ", config.hi_humid_value, "DHT22 Lo Humid ", config.lo_humid_value)
        print("BME280 Hi Humid ", config.hi_humid_value, "BME280 Lo Humid ", config.lo_humid_value)
        
def hi_lo_moisture():
    # reset hi & lo moisture every day @ midnight
    if (config.light_time == "00:00"):
        config.hi_moisture_value = config.moisture
        config.lo_moisture_value = config.moisture
        config.hi_moisture2_value = config.moisture2
        config.lo_moisture2_value = config.moisture2
    # hi moisture value
    if config.moisture > config.hi_moisture_value:
        config.hi_moisture_value = config.moisture
        config.hi_moisture2_value = config.moisture2
    # low moisture value
    if config.moisture < config.lo_moisture_value:
        config.lo_moisture_value = config.moisture
        config.lo_moisture2_value = config.moisture2
        
    if(config.DEBUG):
        print("Hi Moisture ", config.hi_moisture_value, "Lo Moisture ", config.lo_moisture_value)
        print("Hi Moisture2 ", config.hi_moisture2_value, "Lo Moisture2 ", config.lo_moisture2_value)
 
# run main() function
if __name__ == "__main__":
    config.DEBUG = True 
    hi_lo_temp()
    hi_lo_humid()
    hi_lo_moisture()

    # Set the low values
    tempF = 55.0
    humidity = 55.0
    moisture = 200
    moisture2 = 200
    
    hi_lo_temp()
    hi_lo_humid()
    hi_lo_moisture()
