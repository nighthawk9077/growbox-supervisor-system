# The GROWbox Supervisor System (GROWSS)

Todd Moore
Copywrite, 2019 MIT License

### Change Log:

- Date: 19-03-27  Version: V19-03-27-V1A
    - Alpha Version.
    - Original, non-working code.

- Date: 19-04-03  Version: V19-04-03-V1B
    - Beta Version.
    - Working code.
    - Not thoroughly tested.

- Date: 19-04-25  Version: V19-04-25-V1B
    - Beta Version.
    - Working code.
    - Thouroughly tested.
    - Added enable/disable hooks for LCD, LEDs, STDIO, FAN, Light, Water Atomizer
    - Added debug hooks.
    - Added temp hysteresis for controlling exhaust fan

- Date: 19-04-30  Version: V19-04-25-V1B
    - Beta Version
    - Working code
    - Thouroughly tested.
    - Moved time variables to 'config.py'
    - Set initial hi/low values to current values
    - Reset hi/low values every day @ midnight

- Date: 19-05-22  Version: V19-05-20-V1B
    - Creates folder where values saved from the GROWSS app are stored
    - Renamed FAN_HI_HUMID constant to FAN_ON_HUMID to make more sense
    - Separate day & nite temp hysteresis for controlling exhaust fan
    - Humidity hysteresis for controlling exhaust fan
    - Temp & humidity setpoints for Blynk mobile app
        - setpoints for temp & humidity control when exhaust fan turns on
    - Temp & humidity hysteresis for Blynk mobile app
    - Time when lights are on/off for Blynk mobile app

- Date: 20-01-72  Version: Version: V20-01-27
    - Simplified version number
    - swapped MQ2 density sensor with soil moisture sensor
    - added I2C BME280 temp, humid, & pressure sensor
    - modified python code to remove density sensor & add bme280 & moisture sensor.
    - modified Blyk mobile app to remove density widgets & add:
        - bme280 temp, humid, pressure, hi low temp & humid, hi low moisture, bme280 graphs


The GROWSS Website can be found @
<https://sites.google.com/view/thegrowsssystem>

The GROWSS Youtube page can be found @
<https://www.youtube.com/channel/UCl3MO4rn05THPnm7vnGfwRA>

___________________________________________________________________________________________

### This is my design of a GROWbox Supervisor System (GROWSS). The GROWSS system monitors temp, humidty, &soil moisture for 2 potted plants inside a grow box or tent. It also controls the lights, exhaust fan, & hudidifier. An LCD display shows the monitored values.

### A Blynk mobile app is used to monitor the values & alert when thre is an alarm present. The GROWSS Blynk mobile app has only been tested on Andriod mobile phone.

### The GROWSS system will be used in a 2'x2'x6' grow box, but can be used for other sizes of grow box/cabinet/room/tent.

### This design will have many stages until completion.  Check documentation in the 'Files' tab above for detailed descriptions of the design.

### The GROWbox Supervisor System-GROWSS Weppage is here:
#### <https://sites.google.com/view/thegrowsssystem>

### The GROWbox Supervisor System-GROWSS Youtube page is here:
#### <https://www.youtube.com/channel/UCl3MO4rn05THPnm7vnGfwRA/>

### The GROWbox Supervisor System-GROWSS github page is here:
#### <https://github.com/nighthawk9077/growbox-supervisor-system>

### My email:
#### <growbox.supervisor.system.growss@gmail.com>

### The Cannabis Reviewer's Website where you can see the GROWSS in action!
### Follow every week to find out the latest with my cannabis grow here:
##### <https://www.youtube.com/channel/UC_jE8LQd4k3gbLMrVrgcGjg>

### Other relevant links:
#### Raspberry Pi: <http://raspberrypi.org>
#### Grove Sensors: <http://wiki.seeedstudio.com/Grove_System/>
#### Blynk Python Library: <https://github.com/vshymanskyy/blynk-library-python>
#### Blynk Local Server: <https://github.com/blynkkk/blynk-server>

#### Working Design goals are:

- [x] Read Temp (temp/humidity sensor)
- [x] Read Humidity (temp/humidity sensor)
- [x] Read Soil Moisture for 2 plants (soil moisture sensor)
- [x] Visual alarms for over/under values of temp/humidity/soil moisture (leds)
- [x] Save information to local storage as a tab delimeted text file.
- [x] Visual Display (LCD Display)
- [x] Increase humidity in grow box if humidity is too low (humidifier)
- [x] Decrease humidity in grow box if humidity is too high (de-humidifier)
- [x] IoT/Web page/mobile device access/control
- [x] Push alarms to me via text/email
- [x] Turn grow lights on/off using RPI (relay)
- [x] Turn on/off fan based on day or nite temp & humidity using RPI (relay)
- [x] Enable/Disable email, text, fan, light, leds, RGB LCD, & atomizer (humidifier)

#### Icing on the cake would be:

- [ ] Interactive controls for changing env values using blynk app
- [ ] Automatically water plant when soil moisture is too low.
- [ ] Retain values after a crash or reboot.
- [ ] Catch more errors to avoid program crash from broken sensors, etc.
- [ ] Enable/Disable email, text, fan, light, & atomizer (humidifier) from Blynk app.

___________________________________________________________________________________________
FOLDER DESCRIPTIONS FOR THIS REPOSITORY

    - master/ : Design documents & reference documents.
    - Blynk : Folder that contains the Blynk mobile app python examples & modules.
    - blynk_server : Folder that contains the local blynk server & server configuration files.
    - Grove_sensors : Folder that contains information about the sensors being used. Including python examples & modules.
    - Images : Folder that contains various images that were used when creating the documents.
    - RpiDocs : Folder that contains reference documents covering the Raspberry Pi
    - Code : Folder that contains the **MAIN CODE**.

___________________________________________________________________________________________
DOCUMENT DESCRIBING MY JOURNEY DESIGNING, & BUILDING A GROWBOX & THE GROWSS MODULE
    <https://sourceforge.net/projects/growbox-supervisor-system/files/2x2x6%20Foot%20Grow%20Box%20Design.pdf/download>

___________________________________________________________________________________________
DESIGN DOCUMENT & COSTS USING GROVE COMPONENTS
   <https://sourceforge.net/p/growbox-supervisor-system/code/ci/master/tree/GROWbox%20Supervisor%20System.ods>

DESIGN DIAGRAM SHOWING WHERE THE GROVE SENSORS & MODULES & LEDS WILL BE CONNECTED TO THE GROVEPI PLUS HAT
   <https://sourceforge.net/p/growbox-supervisor-system/code/ci/master/tree/GrovePi_Plus_Hat_Sensor%20to%20Pin%20List%20Pin%20Connections.pdf>
   <https://sourceforge.net/p/growbox-supervisor-system/code/ci/master/tree/GrovePi_Plus_Hat_Sensor%20to%20Pin%20List%20Hardware%20Connections.pdf>

THE MAIN CODE
   <https://sourceforge.net/p/growbox-supervisor-system/code/ci/master/tree/>
___________________________________________________________________________________________
Websites for reference:

RPI DOCS
    <https://www.raspberrypi.org/documentation/usage/python/>
    <https://github.com/raspberrypi>

RPI GPIO PINOUT
    <https://pinout.xyz/>

TKINTER GUI WIDGETS CODE
    <https://www.dummies.com/programming/python/using-tkinter-widgets-in-python/>

OTHER GUI LIBRARIES/CODE
    <https://insights.dice.com/2017/08/07/7-top-python-gui-frameworks-for-2017-2/>
    <https://wiki.python.org/moin/WebFrameworks/>

GPIO
    <https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/>
    <http://www.thirdeyevis.com/pi-page-2.php>  - GPIO LED

FILES
    <https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3>

DATE/TIME
    <https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/>
    <https://raspberrypi.stackexchange.com/questions/37802/turn-led-on-after-a-particular-time-for-a-particular-time-period#37807>

EMAIL
    <http://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email>

GROVE SENSOR GITHUB LIBRARY
    <https://github.com/DexterInd/GrovePi>

EXAMPLE PROJECTS
    <https://www.cyber-omelette.com/2017/09/automated-plant-watering.html>
    <https://www.raspberrypi.org/forums/viewtopic.php?t=134395> - Thermostat Hysterisis

IOT USING ANDROID PHONE
Blynk
  <https://www.blynk.cc/>
  <https://github.com/blynkkk/lib-python>
  <https://github.com/vshymanskyy/blynk-library-python>
  <https://www.pibakery.org/>
  <https://github.com/switchdoclabs/SDL_Pi_SmartGardenSystem>  - garden system python code using Blynk

Blynk Local Server Help
    <https://github.com/blynkkk/blynk-server#quick-local-server-setup-on-raspberry-pi>  - install local Blynk server on RPI
    <https://github.com/blynkkk/blynk-server/blob/master/server/core/src/main/resources/server.properties> - commands to use in server.properties for local server setup.
    <https://diyprojects.io/blynk-how-to-install-a-private-local-server-on-raspberry-pi-3-unlimited-energy-test-wemos-dht22/>
    <https://libraries.io/github/blynkkk/blynk-server>
    <https://community.blynk.cc/t/local-server-encryption-setup-file-does-not-contain-valid-private-key-home-pi-blynk-server-pem/25761/4> - Fixing ssl server.pem error when running a local server using self-generated ssl certificates.

RUNNING ARDIUNO SKETCHES C++ (PROGRAMS) ON RPI USING ARDUINO IDE INSTALLED ON LOCAL COMPUTER
    Compile C++ sketches in Arduino on local computer as a binary file that can be copied to the RPI and ran using $ sudo ./sketch.bin
    <https://www.youtube.com/watch?v=lZvhtfUlY8Y>
 
USING FREE VISUAL STUDIO CODE IDE WITH GITHUB
    <https://code.visualstudio.com//#built-in-git>
    <https://code.visualstudio.com/docs/editor/versioncontrol>
    <https://youtu.be/wMqukSKYcvU>                    - Video showing how to use git in Vstudio Code
    <https://www.youtube.com/watch?v=c3482qAzZLQ>     - Not using free version of Vstudio, but good git
                                                        command-line ref anyway

PEP 8 -- STYLE GUIDE FOR PYTHON CODE
    <https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces>
___________________________________________________________________________________________
License
This project is released under The MIT License (MIT)

Copyright 2019 Todd Moore

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
  
  
