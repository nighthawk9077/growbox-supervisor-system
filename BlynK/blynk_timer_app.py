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

BLYNK_AUTH = '9f4faa38d423494fb9c711144e5fea1f'

# data to send to blynk
temp = 75
HI_TEMP = 80	# max allowable temp
LO_TEMP = 65	# min allowable temp
temp_alarm = "YES"
humidity = 75
HI_HUMID = 85	# max allowable humidity percentage
LO_HUMID = 65	# min allowable humidity percentage
humid_alarm = "YES"
moisture = 400
HI_MOISTURE = 700	# max allowable soil moisture level
LO_MOISTURE = 300	# min allowable soil moisture level
moisture_alarm = "YES"
density = 800
HI_DENSITY = 1000	# max allowable air density
smoke_alarm = "YES"
fan_on = "YES"
atomizer_on = "YES"

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pin handler
@blynk.VIRTUAL_READ(0)  # time value
@blynk.VIRTUAL_READ(1)  # temp value
@blynk.VIRTUAL_READ(2)  # hi temp value
@blynk.VIRTUAL_READ(3)  # low temp value
# @blynk.VIRTUAL_READ(4)  # humidity value
# @blynk.VIRTUAL_READ(5)  # hi humidity value
# @blynk.VIRTUAL_READ(6)  # low humidity value
# @blynk.VIRTUAL_READ(7)  # moisture value
# @blynk.VIRTUAL_READ(8)  # hi moisture value
# @blynk.VIRTUAL_READ(9)  # low moisture value
# @blynk.VIRTUAL_READ(10)  # density value
# @blynk.VIRTUAL_READ(11) # hi density value
@blynk.VIRTUAL_READ(12) # smoke alarm
def v2_read_handler():
    if (smoke_alarm == "YES"):
        smoke_led = 255
    else:
        smoke_led = 0
    mytime = datetime.datetime.now().strftime('%H:%M:%S')
    # mytime = datetime.datetime.now().strftime("%Y-%m-%d %I:%M")
    # This widget will show some time in seconds..
    blynk.virtual_write(0, mytime) 
    blynk.virtual_write(1, str(temp))
    blynk.virtual_write(2, str(HI_TEMP))
    blynk.virtual_write(3, str(LO_TEMP))
    # blynk.virtual_write(4, str(humidity))
    # blynk.virtual_write(5, str(HI_HUMID))
    # blynk.virtual_write(6, str(LO_HUMID))
    # blynk.virtual_write(7, str(moisture))
    # blynk.virtual_write(8, str(HI_MOISTURE))
    # blynk.virtual_write(9, str(LO_MOISTURE))
    # blynk.virtual_write(10, str(density))
    # blynk.virtual_write(11, str(HI_DENSITY))
    blynk.virtual_write(12, smoke_led)

while True:
    blynk.run()