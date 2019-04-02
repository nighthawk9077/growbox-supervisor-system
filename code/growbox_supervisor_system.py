"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.
  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app
This example shows how to display custom data on the widget.
In your Blynk App project:
  Add a Value Display widget,
  bind it to Virtual Pin V2,
  set the read frequency to 1 second.
  Run the App (green triangle in the upper right corner).
It will automagically call v2_read_handler.
Calling virtual_write updates widget value.
"""
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
import send_values
import email_handler
import sms_handler

BLYNK_AUTH = '22b066dbfae647e2b0045c6cee0f0943'

########
# Enable flags - Enable/Disable debugging, email, & other features
########
config.DEBUG = False   # debug enable - True prints debugging values during execution
config.email_enable = True # email enable - True turns on email alerts, 
config.text_enable = True   # text enable - True turns on sms text alarts
config.control_fan = True  # enable controlling the fan - True allows RPI to control fan
config.control_moist = True    # control the humidifier - allow RPI to control the water 
                                # atomizer/humidifier
config.control_light = True    # enable controlling the light - True allows RPI to control the lights
config.blynk_app_enable = True # enable sending info to the blynk GROWSS Mobile app
#__________________________________________________________________________________

# Setup Hardware
setup_rpi.hardware()
#__________________________________________________________________________________

# welcome screen on stdio
welcome.startup()
# Welcome Screen on LCD
send_values.version_to_lcd()
#__________________________________________________________________________________

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pin handler
# @blynk.ON(0)
@blynk.VIRTUAL_READ(0)  # time value
@blynk.VIRTUAL_READ(1)  # temp value
@blynk.VIRTUAL_READ(2)  # humidity value
@blynk.VIRTUAL_READ(3)  # moisture value
@blynk.VIRTUAL_READ(4)  # density value
@blynk.VIRTUAL_READ(5)  # hi temp value
@blynk.VIRTUAL_READ(6)  # lo temp value
@blynk.VIRTUAL_READ(7)  # hi humidity value
@blynk.VIRTUAL_READ(8)  # low humidity value
@blynk.VIRTUAL_READ(9)  # hi moisture value
@blynk.VIRTUAL_READ(10)  # lo moisture value
@blynk.VIRTUAL_READ(11) # hi density value
@blynk.VIRTUAL_READ(12) # lo density value
@blynk.VIRTUAL_READ(13)  # hi temp alarm value
@blynk.VIRTUAL_READ(14)  # lo temp alarm value
@blynk.VIRTUAL_READ(15)  # hi humid alarm value
@blynk.VIRTUAL_READ(16)  # lo humid alarm value
@blynk.VIRTUAL_READ(17)  # soil is either: AIR, DRY, PERFECT, WATER
@blynk.VIRTUAL_READ(18)  # hi density (smoke) alarm value
@blynk.VIRTUAL_READ(19)  # hi density (smoke) alarm LED
@blynk.VIRTUAL_READ(20)  # is fan on LED
@blynk.VIRTUAL_READ(21)  # is light on LED
@blynk.VIRTUAL_READ(22)  # is water atomizer on LED

def v2_read_handler():
    # Get current date & times
    config.DATA_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print("Data Date/Time is ", data_time)
    # This widget will show some time in seconds..
    blynk.virtual_write(0, config.DATA_TIME)
    print (config.DATA_TIME)
    minutes = datetime.datetime.now().strftime("%M")
    # print("Minutes is ", minutes)
    light_time = datetime.datetime.now().strftime("%H:%M")  # Only need hours:minutes
    # print("Light Date/Time is ", light_time)
    #__________________________________________________________________________________

    # Get sesor data...
    # Get Temperature in F & Humidity
    get.temp()
    blynk.set_property(1, "label", "CURRENT TEMP")
    blynk.virtual_write(1, str(config.tempF))
    blynk.set_property(2, "label", "CURRENT HUMIDITY")
    blynk.virtual_write(2, str(config.humidity))
    if(config.DEBUG):
        print(config.tempF)
        print(config.humidity)

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
    if(config.DEBUG):
        print(config.moisture)

    # Get Air Quality Value from MQ2 sensor
    get.air()
    blynk.set_property(4, "label", "CURRENT DENSITY")
    blynk.virtual_write(4, str(config.density))
    print(config.density)
    #__________________________________________________________________________________
    # save the hi & low values 
    hi_lo_values.hi_lo_temp()
    blynk.set_property(5, "label", "HI TEMP TODAY")
    blynk.virtual_write(5, str(config.hi_temp_value))
    blynk.set_property(6, "label", "LO TEMP TODAY")
    blynk.virtual_write(6, str(config.lo_temp_value))

    hi_lo_values.hi_lo_humid()
    blynk.set_property(7, "label", "HI HUMID TODAY")
    blynk.virtual_write(7, str(config.hi_humid_value))
    blynk.set_property(8, "label", "LO HUMID TODAY")
    blynk.virtual_write(8, str(config.lo_humid_value))

    hi_lo_values.hi_lo_moisture()
    blynk.set_property(9, "label", "HI MOISTURE TODAY")
    blynk.virtual_write(9, str(config.hi_moisture_value))
    blynk.set_property(10, "label", "LO MOISTURE TODAY")
    blynk.virtual_write(10, str(config.lo_moisture_value))

    hi_lo_values.hi_lo_density()
    blynk.set_property(11, "label", "HI DENSITY TODAY")
    blynk.virtual_write(11, str(config.hi_density_value))
    blynk.set_property(12, "label", "LO DENSITY TODAY")
    blynk.virtual_write(12, str(config.lo_density_value))

    # hi & lo values when alarm is enabled
    blynk.set_property(13, "label", "HI ALARM TEMP")
    blynk.virtual_write(13, str(config.HI_TEMP_ALARM))
    blynk.set_property(14, "label", "LO ALARM TEMP")
    blynk.virtual_write(14, str(config.LO_TEMP_ALARM))

    blynk.set_property(15, "label", "HI ALARM HUMID")
    blynk.virtual_write(15, str(config.HI_HUMID_ALARM))
    blynk.set_property(16, "label", "LO ALARM HUMID")
    blynk.virtual_write(16, str(config.LO_HUMID_ALARM))

    blynk.set_property(17, "label", "SOIL IS ")
    blynk.virtual_write(17, config.moisture_alarm)

    blynk.set_property(18, "label", "HI ALARM DENSITY")
    blynk.virtual_write(18, str(config.HI_DENSITY_ALARM))
    #__________________________________________________________________________________

    # check for alarms
    check_alarms.check_temp()
    blynk.set_property(0, "color", config.blynk_temp_led_color)

    check_alarms.check_humidity()
    blynk.set_property(1, "color", config.blynk_humid_led_color)

    check_alarms.check_moisture()
    blynk.set_property(2, "color", config.blynk_moist_led_color)

    check_alarms.check_gas()
    blynk.set_property(3, "color", config.blynk_smoke_led_color)
    # smoke LED
    blynk.set_property(19, "label", "SMOKE!")
    blynk.set_property(19, "color", config.blynk_smoke_led_color) # smoke LED on gui
    blynk.virtual_write(19, '255')
    #__________________________________________________________________________________

    # control the equipment
    control.fan()
    blynk.set_property(20, "label", "FAN ON")
    blynk.set_property(20, "color", config.blynk_fan_led_color) # fan LED on gui
    blynk.virtual_write(20, '1')

    control.light(light_time)
    blynk.set_property(21, "label", "LIGHT ON")
    blynk.set_property(21, "color", config.blynk_light_led_color) # light LED on gui
    blynk.virtual_write(21, '1')

    control.atomizer()
    blynk.set_property(22, "label", "ATOM ON")
    blynk.set_property(22, "color", config.blynk_atomizer_led_color) # fan LED on gui
    blynk.virtual_write(22, '1')
    #__________________________________________________________________________________

    # save & send values
    # append values to a file every 15 min. a new file is created every day.
    if (minutes == "00" or minutes == "15" or minutes == "30" or minutes == "45"):
        send_values.save_to_file(config.DATA_TIME)

    # print values to std out console
    send_values.print_to_stdio(config.DATA_TIME)

    # output values to the RGB LCD
    # send_values.print_to_LCD(config.DATA_TIME)
    #__________________________________________________________________________________

    # send email if email is enabled & there is an alarm
    if(config.email_enable):
        email_handler.send()

    # send sms text if text is enabled & there is an alarm
    if(config.text_enable):
        sms_handler.send()
    #__________________________________________________________________________________

while True:
    v2_read_handler()
    blynk.run()