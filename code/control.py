########
# control growbox electrical equipment
# Version: 2019-03-27V1A (This is an alpha version & not yet complete
# Todd Moore
# 3.27.19
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

def fan():
    # Turn Fan on if temperature is too high or humidity is too high
    if config.tempF > config.FAN_HI_TEMP or config.humidity > config.FAN_HI_HUMID:
        # turn on exhaust fan. fan is using nc side of relay, so logic is inverted
        config.fan_on = "ON"   # turn on exhaust fan led
        digitalWrite(config.FAN, 0)     # turn on exhaust fan        
        config.blynk_fan_led_color = "#009900"   # LED is GREEN on blynk app
        if(config.DEBUG):
            print("Fan is ",config.fan_on)
            print("fan done")
    else:
        config.fan_on = "OFF"  # turn off exhaust fan led
        # turn off exhaust fan. fan is using nc side of relay, so logic is inverted
        digitalWrite(config.FAN, 1)     
        config.blynk_fan_led_color = "#000000"   # LED is BLACK on blynk app

def atomizer():
    # turn on water atomizer if humidity is too low
    if config.humidity <   config.ATOMIZER_LO_HUMIDITY:
        config.atomizer_on = "ON"
        digitalWrite(config.ATOMIZER, 1)     # turn on atomizer 
        digitalWrite(config.ATOMIZER_ON_LED, 1)     # turn on 'atomizer on' led
        config.blynk_atomizer_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.atomizer_on = "OFF"
        digitalWrite(config.ATOMIZER, 0)     # turn off atomizer 
        digitalWrite(config.ATOMIZER_ON_LED, 0)     # turn off 'atomizer on' led
        config.blynk_atomizer_led_color = "#000000"   # LED is BLACK on blynk app
    if(config.DEBUG):
        print("Atomizer is ", config.atomizer_on)
        print("atomizer done")

def light(light_time):
    # Turn on/off lights at a certain time
    if config.LIGHT_STOP >= light_time >= config.LIGHT_START:
        config.light_on = "ON"
        if(config.DEBUG):
            print(config.LIGHT_START, config.LIGHT_STOP, light_time)
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
    print("Fan Hi Temp Vector is: ", config.FAN_HI_TEMP)
    print("Fan High Humid Vector is: ", config.FAN_HI_HUMID)
    print("Temp & Humidity Vectors are: ", config.tempF, config.humidity)
    fan()
    print("Humidity & Atomizer Low Humidity Vectors are: ", config.humidity, config.ATOMIZER_LO_HUMIDITY)
    atomizer()
    print("Light Date/Time is ", light_time)
    print("Light Start Time & Stop time is: ", config.LIGHT_START, config.LIGHT_STOP)
    light(light_time)
 