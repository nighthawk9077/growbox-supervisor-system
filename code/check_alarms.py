########
# check alarms
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
# # python module that checks temp, humidity, soil moisture, & sets alarms if too high or too low.
# also checks Gas Density & sets smoke alarm if too high.
########

from grovepi import digitalWrite
import config

def check_temp():
    # --------------------------------------------------------------------
    # check for temp alarm
    if config.HI_TEMP_ALARM > config.tempF > config.LO_TEMP_ALARM:
        config.temp_alarm = "OFF"
        config.blynk_temp_led_color = "#009900"   # LED is GREEN on blynk app 
    else:
        config.temp_alarm = "ON"
        config.blynk_temp_led_color = "#FF0000"   # LED is RED on blynk app
    if (config.DEBUG):
        print("Temp Alarm is ", config.temp_alarm)
        print("check_alarms.check_temp done")
   
def check_humidity():
    # --------------------------------------------------------------------
    # check for humidity alarm
    if config.HI_HUMID_ALARM > config.humidity > config.LO_HUMID_ALARM:
        config.humid_alarm = "OFF"
        config.blynk_humid_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.humid_alarm = "ON"
        config.blynk_humid_led_color = "#FF0000"   # LED is RED on blynk app
    if (config.DEBUG):
        print("Humid Alarm is ", config.humid_alarm)
        print("check_alarms.check_humidity done")
        
def check_moisture():
    # --------------------------------------------------------------------
    # Check if there is a soil moisture alarm
    #   Here are suggested sensor values:
    #       Min  Typ  Max  Condition
    #       0    0    0    sensor in open air
    #       0    20   300  sensor in dry soil
    #       300  580  700  sensor in humid soil
    #       700  940  950  sensor in water

    # Human Readable Sensor values: 
    # Values  Condition
    # --------------------------
    # 0-17    'AIR'
    # 18-424  'DRY'
    # 425-689 'HUMID'
    # 690+    'WATER'
    
    # convert moisture value to human readable text 
    if 17 >= config.moisture >= 0:
        config.moisture_alarm = 'AIR'
        config.blynk_moist_led_color = "#CC6600"   # # LED is ORANGE on blynk app
    elif 424 >= config.moisture >= 18:
        config.moisture_alarm = 'DRY'
        config.blynk_moist_led_color = "#CCCC00"   # # LED is YELLOW on blynk app
    elif 689 >= config.moisture >= 425:
        config.moisture_alarm = 'PERFECT'
        config.blynk_moist_led_color = "#009900"   # LED is GREEN on blynk app
    elif config.moisture >= 690:
        config.moisture_alarm = 'WATER'
        config.blynk_moist_led_color = "#0000CC"   # LED is BLUE on blynk app
    if (config.DEBUG):
        print("Moisture Alarm is ", config.moisture_alarm)
        print("check_alarms.check_moisture done")
        
def check_gas():
    # check for smoke alarm
    if config.density < config.HI_DENSITY_ALARM:
        config.smoke_alarm = "OFF"
        config.blynk_smoke_led_color = "#000000"   # LED is BLACK on blynk app
    else:
        config.smoke_alarm = "ON"
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
    