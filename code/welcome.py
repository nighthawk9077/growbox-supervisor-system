########
# welcome module
# Version: 2019-03-27V1A (This is an alpha version & not yet complete
# Todd Moore
# 3.27.19
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# Code is compatible with Python 2.7 and Python 3.5.
# !/usr/bin/env python
# coding=utf-8
########

########
# python module that displays a startup/welcome routine which lights leds, stdio, & lcd
########

from grovepi import digitalWrite
import config
import time

def blink leds():
    # --------------------------------------------------------------------
    # check for temp alarm
    digitalWrite(config.TEMP_ALARM_LED, 1)     # turn on temp alarm led on RPI
    digitalWrite(config.HUMID_ALARM_LED, 1)     # turn on humidity alarm led     
    digitalWrite(config.MOISTURE_ALARM_LED, 1)     # Turn on LED cause soil is VERY dry & needs water!
    digitalWrite(config.SMOKE_ALARM_LED, 1)     # Turn on LED       
    






        
def check_gas():
    # check for smoke alarm
    if config.density < config.HI_DENSITY_ALARM:
        config.smoke_alarm = "OFF"
        digitalWrite(config.BUZZER, 0)     # Turn off buzzer       
        digitalWrite(config.SMOKE_ALARM_LED, 0)     # Turn off buzzer       
        config.blynk_smoke_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.smoke_alarm = "ON"
        digitalWrite(config.BUZZER, 1)     # Turn on buzzer
        digitalWrite(config.SMOKE_ALARM_LED, 0)     # Turn off buzzer       
        config.blynk_smoke_led_color = "#FF0000"   # LED is RED on blynk app
    if (config.DEBUG):
        print("Smoke Alarm is ", config.smoke_alarm)
        print("check_alarms.check_gas done")

# run main() function
if __name__ == "__main__":
    config.DEBUG = True
    check_temp()
    print("High Temp, Low Temp, Temp, & Temp Alarm Vectors are: ", config.HI_TEMP_ALARM, config.LO_TEMP_ALARM, 
            config.tempF, config.temp_alarm)
    
    check_humidity()
    print("High Humid, Low Humid, Humidity, & Humidity Alarm Vectors are: ", config.HI_HUMID_ALARM, 
            config.LO_HUMID_ALARM, config.humidity, config.humid_alarm)
    
    check_moisture()
    print("Moisture is: ", config.moisture)

    check_gas()
    print("High Density, Density, & Smoke Alarm Vectors are: ", config.HI_DENSITY_ALARM, config.density, 
            config.smoke_alarm, config.SMOKE_ALARM_LED)
    