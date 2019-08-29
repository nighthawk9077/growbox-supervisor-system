########
# configuration file
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
# This file contains the configuration values (constants & variables)
########

RPIENVCONTRLR_NAME1 = "THE GROWBOX"
RPIENVCONTRLR_NAME2 = "SUPERVISOR"
RPIENVCONTRLR_NAME3 = "SYSTEM"
RPIENVCONTRLR_NAME4 = "GROWSS"
RPIENVCONTRLR_VER = "19-05-20-V1B"
RPIENVCONTRLR_AUTH = "NIGHTHAWK"
RPIENVCONTRLR_LIC = "2019 MIT"

RPI_NAME = RPIENVCONTRLR_NAME1 + " " + RPIENVCONTRLR_NAME2 + " " + RPIENVCONTRLR_NAME3

BLYNK_AUTH = '9f4faa38d423494fb9c711144e5fea1f'

########
# Enable flags - Enable debugging, email, & other features
########
DEBUG = False   # don't print debugging values during execution
email_enable = False # email enable - True turns on email alerts, 
text_enable = False  # text enable - True sends text alart to mobile phone
leds_enable = True  # True turns on the leds on the case. Turn off for complete darkness
save_to_file_enable = True  # True allows data to be saved to local disk
rgb_lcd_enable = True   # True turns on the led backlight. Turn off for complete darkness

control_fan = True  # enable controlling the fan - True allows RPI to control fan
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
HI_TEMP_ALARM = 95.0    # max allowable temp
LO_TEMP_ALARM = 60.0    # min allowable temp
HI_HUMID_ALARM = 100.0   # max allowable humidity percentage
LO_HUMID_ALARM = 35.0   # min allowable humidity percentage
HI_DENSITY_ALARM = 1000 # max allowable density number

########
# Fan Control Constants
########
FAN_ON_TEMP = 73.0    # temp set point when fan turns on. value changes depending on day or nite.
FAN_DAY_TEMP = 71.0    # temp set point during the day
FAN_NITE_TEMP = 71.0    # temp set point during the nite
FAN_TEMP_HYSTERESIS = 00.5   # temp range fan turns on & off
FAN_ON_HUMID = 55.0   # humidity set point
FAN_HUMID_HYSTERESIS = 00.5   # humidity range fan turns on & off
ATOMIZER_HI_HUMIDITY = 60.0   # humidity set point
ATOM_HUMID_HYSTERESIS = 00.5   # humidity range water atomizer turns on & off

########
# light times
# Germination & Veg is 18 Hrs lights are on & 16 Hrs lights are off
# Flower is 12 Hrs lights on & 12 Hrs lights off
########

LIGHT_START = '08:45'    # turn on light @ 8:45AM
# '20:45'    # turn off light @ 8.45PM
LIGHT_STOP = '02:45'    # turn off light @ 2.45AM
light_time = "00:00"

minutes = "00"

# Folder where stored values file (Values.txt) is written
RetValFolder = './data/'

########
# logged environmental values filename
########
fname_log = 'Values.txt'

########
# measured values
########
tempF = 00.0
hi_temp_value = 90.0
lo_temp_value = 00.0
temp_alarm = "ON"
blynk_temp_led_color = "#FF0000"   # LED is RED on blynk app

humidity = 000.0
hi_humid_value = 000.0
lo_humid_value = 000.0
humid_alarm = "ON"
blynk_humid_led_color = "#FF0000"   # LED is RED on blynk app

moisture = 000
hi_moisture_value = 0000
lo_moisture_value = 0000
moisture_alarm = "AIR"
blynk_moist_led_color = "#CC6600"   # # LED is ORANGE on blynk app

density = 00.00
hi_density_value = 00.0
lo_density_value = 00.0
smoke_alarm = "ON"
blynk_smoke_led_color = "#FF0000"   # LED is RED on blynk app

fan_on = "OFF"   # turn on exhaust fan led
blynk_fan_led_color = "#000000"   # LED is BLACK on blynk app

atomizer_on = "OFF"
blynk_atomizer_led_color = "#000000"   # LED is BLACK on blynk app

light_on = "OFF"
blynk_light_led_color = "#000000"   # LED is BLACK on blynk app

########
# calibration constants
########
temp_calib = 20.0
humidity_calib = 0.0

########
# SMS email & text alert settings
########
growss_email_server = "smtp.gmail.com"
growss_email_port = 587
growss_email_addr = "Your GROWSS email address Here"
growss_email_pwd = "Your GROWSS email password Here"
growss_email_sender_addr = "The sending email address Here"

growss_text_number = "1231231234@vtext.com"
