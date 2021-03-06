########
# control growbox electrical equipment
# Version: V20-02-04 (This is a working BETA vesion): added RH variables code to control 
#   either humidifier or dehumidifier
# Todd Moore
# 2.4.20
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# Code is compatible with Python 2.7 and Python 3.5.
#!/usr/bin/env python
# coding=utf-8
########

########
# control exhaust fan, water atomizer (humidifier), & lights
########

from grovepi import *
import config

# Set fan on temp for either day (lights on) or nite (lights off)
def fan():
    if (config.light_on == "ON"):
        config.FAN_ON_TEMP = config.FAN_DAY_TEMP
    else:
        config.FAN_ON_TEMP = config.FAN_NITE_TEMP
    
    # Turn Fan on if temperature is too high or humidity is too high
    if (config.bme280_tempF > (config.FAN_ON_TEMP + config.FAN_TEMP_HYSTERESIS)
      or config.bme280_humidity > config.FAN_ON_HUMID + config.FAN_HUMID_HYSTERESIS):
        # turn on exhaust fan. fan is using nc side of relay, so logic is inverted
        config.fan_on = "ON"   # turn on exhaust fan led
        digitalWrite(config.FAN, 0)     # turn on exhaust fan        
        config.blynk_fan_led_color = "#009900"   # LED is GREEN on blynk app
    # stop fan from continuously turning on and off
    if (config.bme280_tempF < (config.FAN_ON_TEMP - config.FAN_TEMP_HYSTERESIS) 
      and config.bme280_humidity < config.FAN_ON_HUMID - config.FAN_HUMID_HYSTERESIS):
        config.fan_on = "OFF"  # turn off exhaust fan led
        # turn off exhaust fan. fan is using nc side of relay, so logic is inverted
        digitalWrite(config.FAN, 1)     
        config.blynk_fan_led_color = "#000000"   # LED is BLACK on blynk app

def atomizer():
    if (config.use_humidifier):
        # turn on humidifier if humidity is too low
        if (config.HUMIDIFIER_LO_HUMIDITY -  config.ATOM_HUMID_HYSTERESIS) > config.bme280_humidity:
            config.atomizer_on = "ON"
            digitalWrite(config.ATOMIZER, 1)     # turn on atomizer 
            digitalWrite(config.ATOMIZER_ON_LED, 1)     # turn on 'atomizer on' led
            config.blynk_atomizer_led_color = "#009900"   # LED is GREEN on blynk app
        if (config.HUMIDIFIER_LO_HUMIDITY + config.ATOM_HUMID_HYSTERESIS) < config.bme280_humidity:
            config.atomizer_on = "OFF"
            digitalWrite(config.ATOMIZER, 0)     # turn off atomizer 
            digitalWrite(config.ATOMIZER_ON_LED, 0)     # turn off 'atomizer on' led
            config.blynk_atomizer_led_color = "#000000"   # LED is BLACK on blynk app
    else:
        # turn on de-humidifier if humidity is too high
        if (config.DE_HUMIDIFIER_HI_HUMIDITY + config.ATOM_HUMID_HYSTERESIS) < config.bme280_humidity:
            config.atomizer_on = "ON"
            digitalWrite(config.ATOMIZER, 1)     # turn on de-humidifier 
            digitalWrite(config.ATOMIZER_ON_LED, 1)     # turn on 'atomizer on' led
            config.blynk_atomizer_led_color = "#009900"   # LED is GREEN on blynk app
        if (config.DE_HUMIDIFIER_HI_HUMIDITY -  config.ATOM_HUMID_HYSTERESIS) > config.bme280_humidity:
            config.atomizer_on = "OFF"
            digitalWrite(config.ATOMIZER, 0)     # turn off de-humidifier 
            digitalWrite(config.ATOMIZER_ON_LED, 0)     # turn off 'atomizer on' led
            config.blynk_atomizer_led_color = "#000000"   # LED is BLACK on blynk app

    if(config.DEBUG):
        print("Atomizer is ", config.atomizer_on)
        print("atomizer done")

def light():
    # Turn on/off lights at a certain time
    if config.LIGHT_STOP >= config.light_time >= config.LIGHT_START:
        config.light_on = "ON"
        if(config.DEBUG):
            print(config.LIGHT_START, config.LIGHT_STOP, config.light_time)
        # turn on grow lights. lights using nc side of relay, so logic is inverted
        digitalWrite(config.LIGHT, 0)     # turn on grow light
        config.blynk_light_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.light_on = "OFF"
        # turn off grow lights. lights using nc side of relay, so logic is inverted
        digitalWrite(config.LIGHT, 1)     # turn off grow light
        config.blynk_light_led_color = "#000000"   # LED is BLACK on blynk app
    if(config.DEBUG):
        print("Lights are ", config.light_on)
        print("light done")

def leds():
    # temp alarm led
    if(config.bme280_temp_alarm == "OFF"):
       digitalWrite(config.TEMP_ALARM_LED, 0)     # turn off temp alarm led on RPI
    else:
        digitalWrite(config.TEMP_ALARM_LED, 1)     # turn on temp alarm led on RPI
    # humidity alarm led
    if (config.bme280_humid_alarm == "OFF"):
        digitalWrite(config.HUMID_ALARM_LED, 0)     # turn off humidity alarm led        
    else:
        digitalWrite(config.HUMID_ALARM_LED, 1)     # turn on humidity alarm led     
    # moisture alarm led
    if (config.moisture_alarm == 'PERFECT'):
        digitalWrite(config.MOISTURE_ALARM_LED, 0)     # Turn off LED cause soil is JUST RIGHT!!
    else:
        digitalWrite(config.MOISTURE_ALARM_LED, 1)     # Turn on LED. soil is too dry or wet.

    if (config.moisture2_alarm == 'PERFECT'):
        digitalWrite(config.MOISTURE2_ALARM_LED, 0)     # Turn off LED cause soil is JUST RIGHT!!
    else:
        digitalWrite(config.MOISTURE2_ALARM_LED, 1)     # Turn on LED. soil is too dry or wet.

# run main() function
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    import datetime
    import config

    config.DEBUG = True
    pinMode(config.LIGHT,"OUTPUT")
    pinMode(config.FAN,"OUTPUT")
    pinMode(config.ATOMIZER,"OUTPUT")
    pinMode(config.ATOMIZER_ON_LED,"OUTPUT")
    time.sleep(1)
    
    light_time = datetime.datetime.now().strftime("%H:%M")
    print("Fan On Temp Vector is: ", config.FAN_ON_TEMP)
    print("Fan High Humid Vector is: ", config.FAN_ON_HUMID)
    print("Temp & Humidity Vectors are: ", config.bme280_tempF, config.bme280_humidity)
    fan()
    print("Humidity & Atomizer Low Humidity Vectors are: ", config.bme280_humidity, config.ATOM_HUMID_HYSTERESIS)
    atomizer()
    print("Light Date/Time is ", light_time)
    print("Light Start Time & Stop time is: ", config.LIGHT_START, config.LIGHT_STOP)
    light()
 