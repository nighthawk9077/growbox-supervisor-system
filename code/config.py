########
# configuration file
# Version: V20-02-04 (This is a working BETA vesion): added RH variables code to control 
#   either humidifier or dehumidifier
# Todd Moore
# 2.4.20
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
# This file contains the configuration values (constants & variables)
########

RPIENVCONTRLR_NAME1 = "THE GROWBOX"
RPIENVCONTRLR_NAME2 = "SUPERVISOR"
RPIENVCONTRLR_NAME3 = "SYSTEM"
RPIENVCONTRLR_NAME4 = "GROWSS"
RPIENVCONTRLR_VER = "20-01-20-V2B"
RPIENVCONTRLR_AUTH = "NIGHTHAWK/CANNABIS REVIEWER"
RPIENVCONTRLR_LIC = "2020 MIT"

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
use_humidifier = True   # either use the humidifier or use the de-humdifier
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
MOISTURE2_ALARM_LED = 8
MOISTURE_ALARM_LED = 9
FAN = 16    # uses A2 as digital channels 16 & 17
LIGHT = 17  # uses A2 as digital channels 16 & 17

########
# GrovePi+ Hat Analog Pin Constants
########
MOISTURE_SENSOR = 0
MOISTURE_SENSOR2 = 1  

########
# temp_humidity_sensor_type
# This represents the cover color of the sensor. I have the white type.
########
# #BLUE = 0    # The Blue colored sensor.
WHITE = 1   # The White colored sensor.

########
# #Software constants
########
# DHT22
DATA_TIME = "10:00:00 00:00:00"
HI_TEMP_ALARM = 95.0    # max allowable temp
LO_TEMP_ALARM = 60.0    # min allowable temp
HI_HUMID_ALARM = 100.0   # max allowable humidity percentage
LO_HUMID_ALARM = 25.0   # turn on humid alarm when humid is <=

# BME280 constants
BME280_HI_TEMP_ALARM = 95.0    # max allowable temp
BME280_LO_TEMP_ALARM = 60.0    # min allowable temp
BME280_HI_HUMID_ALARM = 100.0   # max allowable humidity percentage
BME280_LO_HUMID_ALARM = 10.0    # turn on bme280 humid alarm when humid is <=

########
# Fan Control Constants
########
FAN_ON_TEMP = 75.0    # temp set point when fan turns on. value changes depending on day or nite.
FAN_DAY_TEMP = 76.0    # temp set point during the day
FAN_NITE_TEMP = 76.0    # temp set point during the nite
FAN_TEMP_HYSTERESIS = 00.5   # temp range fan turns on & off
FAN_ON_HUMID = 70.0   # humidity set point
FAN_HUMID_HYSTERESIS = 05.0   # humidity range fan turns on & off
HUMIDIFIER_LO_HUMIDITY = 65.0   # turn on the humidifier at this temp +/- ATOM_HUMID_HYSTERESIS
DE_HUMIDIFIER_HI_HUMIDITY = 65.0   #  # turn on the humidifier at this temp +/- ATOM_HUMID_HYSTERESIS
ATOM_HUMID_HYSTERESIS = 02.0   # humidity range water atomizer turns on & off


########
# light times
# Germination & Veg is 18 Hrs lights are on & 16 Hrs lights are off
# Flower is 12 Hrs lights on & 12 Hrs lights off
########
# LIGHT_START = '09:00'    # turn on light @ 9:00AM
# LIGHT_STOP = '21:00'    # turn off light @ 9:00PM - 12/12 ON/OFF
# FLR_LIGHT_STOP = '20:45'    # turn off light @ 8:45AM - 12/12 ON/OFF
LIGHT_START = '06:00'    # turn on light @ 6:00AM
LIGHT_STOP = '23:59'    # turn off light @ 11:59PM - 12/12 ON/OFF
light_time = "00:00"
minutes = "00"
# grow_cycle = "VEG"

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

moisture2 = 000
hi_moisture2_value = 0000
lo_moisture2_value = 0000
moisture2_alarm = "AIR"
blynk_moist2_led_color = "#CC6600"   # # LED is ORANGE on blynk app

# ********* BME280 measured values *********************
bme280_chip_id = 00
bme280_chip_version = 0

bme280_tempC = 00.0
bme280_temperature = 00.0
bme280_tempF = 00.0
bme280_hi_temp_value = 90.0
bme280_lo_temp_value = 00.0
bme280_temp_alarm = "ON"
blynk_bme280_temp_led_color = "#FF0000"   # LED is RED on blynk app

bme280_humidity = 000.0
bme280_hi_humid_value = 000.0
bme280_lo_humid_value = 000.0
bme280_humid_alarm = "ON"
blynk_bme280_humid_led_color = "#FF0000"   # LED is RED on blynk app

bme280_pressure = 0000.00
blynk_bme280_pressure_led_color = "#00FF00"   # LED is Lime on blynk app

fan_on = "OFF"   # turn on exhaust fan led
blynk_fan_led_color = "#000000"   # LED is BLACK on blynk app

atomizer_on = "OFF"
blynk_atomizer_led_color = "#000000"   # LED is BLACK on blynk app

light_on = "OFF"
blynk_light_led_color = "#000000"   # LED is BLACK on blynk app

########
# SMS email & text alert settings
########
growss_email_server = "smtp.gmail.com"
growss_email_port = 587
growss_email_addr = "Your GROWSS email address Here"
growss_email_pwd = "Your GROWSS email password Here"
growss_email_sender_addr = "The sending email address Here"

growss_text_number = "1231231234@vtext.com"
