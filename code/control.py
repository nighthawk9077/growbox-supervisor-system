# control.py
# Todd Moore
# 3.9.19

# ******** WORKING AS OF 3.17.19 *****
# control exhaust fan, water atomizer (humidifier), & lights

from grovepi import *
import config

def fan():
    # Turn Fan on if temperature is too high or humidity is too high
    if config.FAN_HI_TEMP > config.tempF > config.FAN_LO_TEMP:
        config.fan_on = "OFF"  # turn off exhaust fan led
        digitalWrite(config.FAN, 0)     # turn off exhaust fan   
        config.blynk_fan_led_color = "#000000"   # LED is BLACK on blynk app
    else:
        config.fan_on = "ON"   # turn on exhaust fan led
        digitalWrite(config.FAN, 1)     # turn on exhaust fan        
        config.blynk_fan_led_color = "#009900"   # LED is GREEN on blynk app
    # print("Fan is ",fan_on)
    # print("fan done")
#    return fan_on, blynk_fan_led_color

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
    # print("Atomizer is ", atomizer_on)
    # print("atomizer done")
#    return atomizer_on, blynk_atomizer_led_color

def light(light_time):
    # Turn on/off lights at a certain time
    if config.LIGHT_STOP > light_time > config.LIGHT_START:
        config.light_on = "ON"
        print(config.LIGHT_START, config.LIGHT_STOP, config.light_time)
        digitalWrite(config.LIGHT, 1)     # turn on grow light
        config.blynk_light_led_color = "#009900"   # LED is GREEN on blynk app
    else:
        config.light_on = "OFF"
        digitalWrite(config.LIGHT, 0)     # turn off grow light
        config.blynk_light_led_color = "#000000"   # LED is BLACK on blynk app
     # print("Lights are ", light_on)
    # print("light done")
#    return light_on, blynk_light_led_color

# run main() function
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    import datetime
    import config

    pinMode(config.LIGHT,"OUTPUT")
    pinMode(config.FAN,"OUTPUT")
    pinMode(config.ATOMIZER,"OUTPUT")
    pinMode(config.ATOMIZER_ON_LED,"OUTPUT")
    time.sleep(1)
    
    light_time = datetime.datetime.now().strftime("%H:%M")
    print("Fan Hi Temp, & Fan Low Temp Vectors are: ", config.FAN_HI_TEMP, config.FAN_LO_TEMP)
    print("Fan High Humid, & Fan Low Humid Vectors are: ", config.FAN_HI_HUMID, config.FAN_LO_HUMID)
    print("Temp & Humidity Vectors are: ", config.tempF, config.humidity)
    fan()
    print("Humidity & Atomizer Low Humidity Vectors are: ", config.humidity, config.ATOMIZER_LO_HUMIDITY)
    atomizer()
    print("Light Date/Time is ", config.light_time)
    print("Light Start Time & Stop time is: ", config.LIGHT_START, config.LIGHT_STOP)
    light()
 