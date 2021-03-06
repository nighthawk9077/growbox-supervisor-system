########
# The GROWbox Supervisor System (GROWSS)
# Version: V20-02-04 (This is a working BETA vesion): added RH control constants 
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
# The GROWbox Supervisor System (GROWSS) is a monitor & control system for small to medium grow boxes
# & grow cabinets. GROWSS uses a Raspberry Pi SBC, a GrovePi+ Hat, & Grove Sensors to monitor and
# control the growing environment.
#
# Features Include:
#    - Monitor Temperature, Humidity, Pressure, & soil moisture.  Measurements are taken about every 25 
#      seconds and updated to the displays (below).
#    - Density (smoke alarm) sensor has been removed and replaced with an additional soil moisture sensor.
#    - Controls growing lights, exhaust fan, & humidifier.
#       - Turns lights on & off based on time.
#       - Turns exhaust fan on & off based on either day (lights on) or nite (lights off) temp & humidity.
#       - Turns water atomizer (humidifier) or de-humidifier on & off based on humidity.
#    - Sets alarms for hi/low temperature, humidity & soil moisture.
#    - Monitoring & Alarm information is provided many ways:
#       - All measured values can be saved to local storage every 15 min.
#       - LEDs on the front indicate if there is a temperature, humidity, or soil moisture alarm.
#       - LEDs on the front also indicate when the exhaust fan is on & when the humidifier is running.
#       - An RGB LCD on the case dispalys the growing information in an easy to see format.
#       - A mobile app is also available to monitor the growing environment with alarms & hi/low values.
#       - Send email and/or text if an alarm is present.
#       - Enable/Disable email, text, fan, light, & atomizer (humidifier). Currently has to be changed
#           in the code below.
########

########
# Features maybe included in the future:
#   - Automatically water plant when soil moisture is too low.
#   - Ability to change alarm threasholds easily (ie. switch, etc.)
#   - Enable/Disable email, text, fan, light, & atomizer (humidifier) from Blynk app.
#   - Retain values after a crash or reboot.
#   - Catching more errors to avoid program crash from broken sensors, etc.
########

########
# RPI/Grove+ Pinout Definitions

#   Port #  Pins on Port #  Type                Sensor Pin  Sensor/Module
#   ------------------------------------------------------------------------
#   SERIAL  D0 & D1         DIGITAL & SERIAL                n/a
#   D2      D2 & D3         DIGITAL             D2          Grove Buzzer
#   D3      D3 & D4         DIGITAL             D3          Humid Alarm LED
#                                               D4          Temp Alarm LED
#   D4      D4 & D5         DIGITAL             n/a
#   D5      D5 & D6         DIGITAL             D5          Water Atomizer LED
#   D6      D6 & D7         DIGITAL             D6          Grove - Temperature&Humidity Sensor Pro
#   D7      D7 & D8         DIGITAL             D7          Grove - 1-Channel SPDT Switch 1, Humidifier
#   D8      D8 & D9         DIGITAL             D8          Smoke Alarm LED
#                                               D9          Moisture Alarm LED
#                   
#   A0      A0 & A1         ANALOG              A0          Grove - Moisture Sensor #1
#   A1      A1 & A2         ANALOG              A1          Grove - Moisture Sensor #2 
#                                                           (MQ2 Air Sensor was removed)
#   A2      A2 & A3         ANALOG              D16         Grove - 2-Channel SPDT Switch 1,
#                                                               LED Lights
#                                               D17         Grove - 2-Channel SPDT Switch 2,
#                                                               Exhaust Fan
#
#   I2C-1   I2C                                             Free
#   I2C-2   I2C                                             BME280 Temperature, Humidity, & Pressure sensor
#   I2C-3   I2C                                             Grove - LCD RGB Backlight
#   RPRISER                 RPI SERIAL          
########
import create_folder
import datetime
import BlynkLib
import config
import setup_rpi
import welcome
import send_values
import get
import hi_lo_values
import check_alarms
import control
import email_handler
import sms_handler
from grove_rgb_lcd import *
from grovepi import digitalWrite

BLYNK_AUTH = '22b066dbfae647e2b0045c6cee0f0943'

########
# Enable flags - Enable/Disable debugging, email, & other features
########
config.DEBUG = False   # debug enable - True prints debugging values during execution
config.email_enable = False # email enable - True turns on email alerts, 
config.text_enable = False   # text enable - True turns on sms text alarts
config.leds_enable = False  # True turns on the leds on the case. Turn off for complete darkness
config.rgb_lcd_enable = True   # True turns on the led backlight. Turn off for complete darkness
config.save_to_file_enable = False  # True allows data to be saved to local disk

config.control_fan = True  # enable controlling the fan - True allows RPI to control fan
config.control_atomizer = True    # control the humidifier - allow RPI to control the water 
                                # atomizer/humidifier
config.use_humidifier = False # determines whether humidifier or de-humidifier is being used
config.control_light = True    # enable controlling the light - True allows RPI to control the lights
#__________________________________________________________________________________

# Setup Hardware
setup_rpi.hardware()
#__________________________________________________________________________________

# welcome screen on stdio
# welcome.startup()
# Welcome Screen on LCD
#send_values.version_to_lcd()
#__________________________________________________________________________________

# Creates a folder in the current directory for retaining values if none exists
# Also creates new data file if none exists
create_folder.createFolder(config.RetValFolder)
#__________________________________________________________________________________

# set baseline temp hi/lo levels first time thru
get.dht22_values()
config.hi_temp_value = config.tempF
config.lo_temp_value = config.tempF
config.hi_humid_value = config.humidity
config.lo_humid_value = config.humidity

get.bme280_values()
config.bme280_hi_temp_value = config.bme280_tempF
config.bme280_lo_temp_value = config.bme280_tempF
config.bme280_hi_humid_value = config.bme280_humidity
config.bme280_lo_humid_value = config.bme280_humidity
#__________________________________________________________________________________

# set baseline soil moisture hi/lo levels first time thru
get.moisture()
config.hi_moisture_value = config.moisture
config.lo_moisture_value = config.moisture
config.hi_moisture2_value = config.moisture2
config.lo_moisture2_value = config.moisture2
#__________________________________________________________________________________

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pins
@blynk.VIRTUAL_READ(0)  # time value
@blynk.VIRTUAL_READ(1)  # temp value
@blynk.VIRTUAL_READ(2)  # humidity value
@blynk.VIRTUAL_READ(3)  # moisture value
@blynk.VIRTUAL_READ(4)  # moisture2 value
@blynk.VIRTUAL_READ(5)  # hi temp value
@blynk.VIRTUAL_READ(6)  # lo temp value
@blynk.VIRTUAL_READ(7)  # hi humidity value
@blynk.VIRTUAL_READ(8)  # low humidity value
@blynk.VIRTUAL_READ(9)  # hi moisture value
@blynk.VIRTUAL_READ(10)  # lo moisture value
@blynk.VIRTUAL_READ(11) # hi moisture2 value
@blynk.VIRTUAL_READ(12) # lo moisture2 value
@blynk.VIRTUAL_READ(13)  # hi temp alarm value
@blynk.VIRTUAL_READ(14)  # lo temp alarm value
@blynk.VIRTUAL_READ(15)  # hi humid alarm value
@blynk.VIRTUAL_READ(16)  # lo humid alarm value
@blynk.VIRTUAL_READ(17)  # soil is either: AIR, DRY, PERFECT, WATER
@blynk.VIRTUAL_READ(18)  # humid value when atomizer turns on/off
@blynk.VIRTUAL_READ(19)  # soil 2 is either: AIR, DRY, PERFECT, WATER
@blynk.VIRTUAL_READ(20)  # is fan on LED
@blynk.VIRTUAL_READ(21)  # is light on LED
@blynk.VIRTUAL_READ(22)  # is water atomizer on LED
@blynk.VIRTUAL_READ(23)  # software acronym
@blynk.VIRTUAL_READ(24)  # software name
@blynk.VIRTUAL_READ(25)  # software version
@blynk.VIRTUAL_READ(26)  # software author
@blynk.VIRTUAL_READ(27)  # device license
@blynk.VIRTUAL_READ(28)  # temp setpoint that turns fan on
@blynk.VIRTUAL_READ(29)  # humid setpoint that turns fan on
@blynk.VIRTUAL_READ(30)  # temp hysteresis
@blynk.VIRTUAL_READ(31)  # humidity hysteresis
@blynk.VIRTUAL_READ(32)  # when the lights turn on
@blynk.VIRTUAL_READ(33)  # when the lights turn off

@blynk.VIRTUAL_READ(34)  # bme280 temp
@blynk.VIRTUAL_READ(35)  # bme280 humidity
@blynk.VIRTUAL_READ(36)  # bme280 pressure
@blynk.VIRTUAL_READ(37)  # bme280 hi daily temp
@blynk.VIRTUAL_READ(38)  # bme280 lo daily temp
@blynk.VIRTUAL_READ(39)  # bme280 hi daily humidity
@blynk.VIRTUAL_READ(40)  # bme280 lo daily humidity
#__________________________________________________________________________________

def v2_read_handler():
    # Get current date & times
    config.DATA_TIME = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    # This widget will show some time in seconds..
    blynk.virtual_write(0, config.DATA_TIME)
    config.minutes = datetime.datetime.now().strftime("%M")
    config.light_time = datetime.datetime.now().strftime("%H:%M")  # Only need hours:minutes
    if(config.DEBUG):
        print("Data Date/Time is ", config.DATA_TIME)
        print("Minutes is ", config.minutes)
        print("Light Date/Time is ", config.light_time)
    #__________________________________________________________________________________

    # send software info to blynk
    blynk.set_property(23, "color", "#009900") # green
    blynk.set_property(23, "label", "NAME:")
    blynk.virtual_write(23, config.RPIENVCONTRLR_NAME4)
    blynk.virtual_write(24, config.RPI_NAME)
    blynk.set_property(25, "label", "VERSION:")
    blynk.virtual_write(25, config.RPIENVCONTRLR_VER)
    blynk.set_property(26, "label", "AUTHOR:")
    blynk.virtual_write(26, config.RPIENVCONTRLR_AUTH)
    blynk.set_property(27, "label", "COPYWRITE LIC:")
    blynk.virtual_write(27, config.RPIENVCONTRLR_LIC)
    #__________________________________________________________________________________

    # Get sesor data...
    # Get Temperature in F & Humidity from the DHT22 sensor
    get.dht22_values()
    blynk.set_property(1, "label", "DHT22 CURRENT TEMP")
    blynk.virtual_write(1, str(config.tempF))
    blynk.set_property(2, "label", "DHT22 CURRENT HUMIDITY")
    blynk.virtual_write(2, str(config.humidity))

    # Get Temperature in F, Humidity, & Pressure from the BME280 sensor
    get.bme280_values()
    blynk.set_property(34, "label", "BME280 CURRENT TEMP")
    blynk.virtual_write(34, str(config.bme280_tempF))
    blynk.set_property(35, "label", "BME280 CURRENT HUMIDITY")
    blynk.virtual_write(35, str(config.bme280_humidity))
    blynk.set_property(36, "label", "BME280 CURRENT PRESS")
    blynk.virtual_write(36, str(config.bme280_pressure))

    # Get Soil Moisture & check if there is an alarm
    #   Here are suggested sensor values:
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
    get.moisture()
    blynk.set_property(3, "label", "CURRENT MOISTURE")
    blynk.virtual_write(3, str(config.moisture))
    blynk.set_property(4, "label", "CURRENT MOISTURE 2")
    blynk.virtual_write(4, str(config.moisture2))
    #__________________________________________________________________________________
    
    # save the hi & low values 
    hi_lo_values.hi_lo_temp()
    blynk.set_property(5, "label", "HI TEMP")
    blynk.virtual_write(5, str(config.hi_temp_value))
    blynk.set_property(6, "label", "LO TEMP")
    blynk.virtual_write(6, str(config.lo_temp_value))
    blynk.set_property(37, "label", "BME280 HI TEMP")
    blynk.virtual_write(37, str(config.bme280_hi_temp_value))
    blynk.set_property(38, "label", "BME280 LO TEMP")
    blynk.virtual_write(38, str(config.bme280_lo_temp_value))

    hi_lo_values.hi_lo_humid()
    blynk.set_property(7, "label", "HI HUMID")
    blynk.virtual_write(7, str(config.hi_humid_value))
    blynk.set_property(8, "label", "LO HUMID")
    blynk.virtual_write(8, str(config.lo_humid_value))
    blynk.set_property(39, "label", "BME280 HI HUMID")
    blynk.virtual_write(39, str(config.bme280_hi_humid_value))
    blynk.set_property(40, "label", "BME280 LO HUMID")
    blynk.virtual_write(40, str(config.bme280_lo_humid_value))

    hi_lo_values.hi_lo_moisture()
    blynk.set_property(9, "label", "HI MOISTURE")
    blynk.virtual_write(9, str(config.hi_moisture_value))
    blynk.set_property(10, "label", "LO MOISTURE")
    blynk.virtual_write(10, str(config.lo_moisture_value))
    blynk.set_property(11, "label", "HI MOISTURE 2")
    blynk.virtual_write(11, str(config.hi_moisture2_value))
    blynk.set_property(12, "label", "LO MOISTURE 2")
    blynk.virtual_write(12, str(config.lo_moisture2_value))

    blynk.set_property(13, "label", "HI TEMP ALARM ")
    blynk.virtual_write(13, str(config.HI_TEMP_ALARM))
    blynk.set_property(14, "label", "LO TEMP ALARM ")
    blynk.virtual_write(14, str(config.LO_TEMP_ALARM))

    blynk.set_property(15, "label", "HI HUMID ALARM ")
    blynk.virtual_write(15, str(config.HI_HUMID_ALARM))
    blynk.set_property(16, "label", "LO HUMID ALARM ")
    blynk.virtual_write(16, str(config.LO_HUMID_ALARM))

    if(config.control_atomizer):
        if(config.use_humidifier):
            blynk.set_property(18, "label", "HUMID ON RH%")
            blynk.virtual_write(18, str(config.HUMIDIFIER_LO_HUMIDITY))
        else:
            blynk.set_property(18, "label", "DHUMID ON RH%")
            blynk.virtual_write(18, str(config.HUMIDIFIER_LO_HUMIDITY))
    #__________________________________________________________________________________

    # check for alarms
    check_alarms.check_temp()
    blynk.set_property(1, "color", config.blynk_temp_led_color)

    check_alarms.check_humidity()
    blynk.set_property(2, "color", config.blynk_humid_led_color)

    check_alarms.check_moisture()
    blynk.set_property(3, "color", config.blynk_moist_led_color)
    blynk.set_property(17, "label", "SOIL #1 IS ")
    blynk.set_property(17, "color", config.blynk_moist_led_color)
    blynk.virtual_write(17, config.moisture_alarm)

    blynk.set_property(4, "color", config.blynk_moist2_led_color)
    blynk.set_property(19, "label", "SOIL #2 IS ")
    blynk.set_property(19, "color", config.blynk_moist2_led_color) # soil moisture 2 LED on gui
    blynk.virtual_write(19, config.moisture2_alarm)
    #__________________________________________________________________________________

    # control the equipment
    if(config.leds_enable):
        control.leds()
    else:
        digitalWrite(config.TEMP_ALARM_LED, 0)     # turn off temp alarm led on RPI
        digitalWrite(config.HUMID_ALARM_LED, 0)     # turn off humidity alarm led        
        digitalWrite(config.MOISTURE_ALARM_LED, 0)     # Turn off LED cause soil is JUST RIGHT!!
        digitalWrite(config.MOISTURE2_ALARM_LED, 0)     # Turn off LED cause soil is JUST RIGHT!!     
    
    if(config.control_fan):
        control.fan()
        blynk.set_property(20, "label", "FAN")
        blynk.set_property(20, "color", config.blynk_fan_led_color) # fan LED on gui
    else:
        blynk.set_property(20, "label", "DIS")
        blynk.set_property(20, "color", "#808080") # fan LED is disabled
    blynk.virtual_write(20, '255')  # turn led on

    blynk.set_property(28, "color", "#4682B4") # steel blue
    blynk.set_property(28, "label", "FAN ON TEMP")
    blynk.virtual_write(28, str(config.FAN_ON_TEMP)) # temp (+/- hysteresis) when fan turns on
    blynk.set_property(29, "color", "#4682B4") # steel blue
    blynk.set_property(29, "label", "FAN ON HUMID:")
    blynk.virtual_write(29, str(config.FAN_ON_HUMID)) # humidity (+/- hysteresis) when fan turns on
    blynk.set_property(30, "color", "#6495ED") # corn flower blue
    blynk.set_property(30, "label", "TEMP HYSTERESIS:")
    blynk.virtual_write(30, str(config.FAN_TEMP_HYSTERESIS)) # temp hysteresis
    blynk.set_property(31, "color", "#6495ED") # green
    blynk.set_property(31, "label", "HUMID HYSTERESIS:")
    blynk.virtual_write(31, str(config.FAN_HUMID_HYSTERESIS)) # humidity hysteresis

    if(config.control_light):
        control.light()
        blynk.set_property(21, "label", "LIGHT")
        blynk.set_property(21, "color", config.blynk_light_led_color) # light LED on gui
    else:
        blynk.set_property(21, "label", "DIS")
        blynk.set_property(21, "color", "#808080") # light LED is disabled
    blynk.virtual_write(21, '255')
    
    blynk.set_property(32, "color", "#FFD700") # gold
    blynk.set_property(32, "label", "LIGHTS ON TIME:")
    blynk.virtual_write(32, str(config.LIGHT_START)) # when lights turns on
    blynk.set_property(33, "color", "#FFD700") # gold
    blynk.set_property(33, "label", "LIGHTS OFF TIME:")
    blynk.virtual_write(33, str(config.LIGHT_STOP)) # when lights turns off

    if(config.control_atomizer):
        if(config.use_humidifier):
            blynk.set_property(22, "label", "HUMID")
        else:
            blynk.set_property(22, "label", "DE_H")
        control.atomizer()
        blynk.set_property(22, "color", config.blynk_atomizer_led_color) # atomizer LED on gui
    else:
        blynk.set_property(22, "label", "DIS")
        blynk.set_property(22, "color", "#808080") # atomizer LED is disabled
    blynk.virtual_write(22, '255')
    

    # control.buzzer()
    #__________________________________________________________________________________

    # append values to a file every 15 min. a new file is created every day.
    if(config.save_to_file_enable):
        if (config.minutes == "00" or config.minutes == "15" or config.minutes == "30" or config.minutes == "45"):
            send_values.save_to_file()

    # print values to std out console
    if(config.DEBUG): send_values.print_to_stdio()

    # output values to the RGB LCD
    if(config.rgb_lcd_enable): send_values.print_to_LCD()
    else:
        setRGB(0,0,0) # display is black
    #__________________________________________________________________________________

    # send email if email is enabled & there is an alarm
    if(config.email_enable): email_handler.send()

    # send sms text if text is enabled & there is an alarm
    if(config.text_enable): sms_handler.send()
    #__________________________________________________________________________________

while True:
    v2_read_handler()
    blynk.run()
