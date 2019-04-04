########
# configuration file
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
# This file contains the configuration values (constants & variables)
########

RPIENVCONTRLR_NAME1 = "THE GROWBOX"
RPIENVCONTRLR_NAME2 = "SUPERVISOR"
RPIENVCONTRLR_NAME3 = "SYSTEM"
RPIENVCONTRLR_NAME4 = "GROWSS"
RPIENVCONTRLR_VER = "19-04-03-V1B"
RPIENVCONTRLR_AUTH = "NIGHTHAWK"
RPIENVCONTRLR_LIC = "2019 MIT"

RPI_NAME = RPIENVCONTRLR_NAME1 + " " + RPIENVCONTRLR_NAME2 + " " + RPIENVCONTRLR_NAME3

#BLYNK_AUTH = 'e4a966c887854bb4b4c888af727579fd'
BLYNK_AUTH = '22b066dbfae647e2b0045c6cee0f0943'

########
# Enable flags - Enable debugging, email, & other features
########
DEBUG = False   # don't print debugging values during execution
email_enable = False # email enable - True turns on email alerts, 
text_enable = False  # text enable - True sends text alart to mobile phonecontrol_fan = True  # enable controlling the fan - True allows RPI to control fan
control_atomizer = True    # control the humidifier - allow RPI to control the water atomizer/humidifier
control_light = True    # enable controlling the light - True allows RPI to control the lights

########
# Setup Constants
# GrovePi+ Hat Digital Pin Constants
########
BUZZER = 2          
HUMID_ALARM_LED = 3
TEMP_ALARM_LED = 4
ATOMIZER_ON_LED = 5
TEMP_SENSOR = 6
ATOMIZER = 7
SMOKE_ALARM_LED = 8
MOISTURE_ALARM_LED = 9
FAN = 16    # uses A2 as digital channels 16 & 17
LIGHT = 17  # uses A2 as digital channels 16 & 17

########
# GrovePi+ Hat Analog Pin Constants
########
MOISTURE_SENSOR = 0
GAS_SENSOR = 1  

########
# temp_humidity_sensor_type
# This represents the cover color of the sensor. I have the white type.
########
# #BLUE = 0    # The Blue colored sensor.
WHITE = 1   # The White colored sensor.

########
# #Software constants
########
DATA_TIME = "10:00:00 00:00:00"
HI_TEMP_ALARM = 70.0    # max allowable temp
LO_TEMP_ALARM = 40.0    # min allowable temp
HI_HUMID_ALARM = 75.0   # max allowable humidity percentage
LO_HUMID_ALARM = 25.0   # min allowable humidity percentage
HI_DENSITY_ALARM = 1000 # max allowable density number
FAN_HI_TEMP = 80.0    # max allowable temp before fan turns on
FAN_HI_HUMID = 85.0   # lowest allowable humidity percentage before fan turns on
ATOMIZER_LO_HUMIDITY = 10.0   # humidity level water atomizer turns on
LIGHT_START = '05:00'    # turn on light @ 5AM
LIGHT_STOP = '16:00'    # turn off light @ 5PM

########
# measured values
########
tempF = 00.0
hi_temp_value = 00.0
lo_temp_value = 90.0
temp_alarm = "ON"
blynk_temp_led_color = "#FF0000"   # LED is RED on blynk app

humidity = 000.0
hi_humid_value = 000.0
lo_humid_value = 090.0
humid_alarm = "ON"
blynk_humid_led_color = "#FF0000"   # LED is RED on blynk app

moisture = 000
hi_moisture_value = 000
lo_moisture_value = 100
moisture_alarm = "AIR"
blynk_moist_led_color = "#CC6600"   # # LED is ORANGE on blynk app

density = 00.00
hi_density_value = 00.0
lo_density_value = 50.0
smoke_alarm = "ON"
blynk_smoke_led_color = "#FF0000"   # LED is RED on blynk app

fan_on = "ON"   # turn on exhaust fan led
blynk_fan_led_color = "#009900"   # LED is GREEN on blynk app

atomizer_on = "OFF"
blynk_atomizer_led_color = "#000000"   # LED is BLACK on blynk app

light_on = "OFF"
blynk_light_led_color = "#000000"   # LED is BLACK on blynk app


########
# SMS email & text alert settings
########
growss_email_server = "smtp.gmail.com"
growss_email_port = 587
growss_email_addr = "growbox.supervisor.system.growss@gmail.com"
growss_email_pwd = "grows.alot.420"
growss_email_sender_addr = "todd9077@gmail.com"

growss_text_number = "2174935571@vtext.com"
