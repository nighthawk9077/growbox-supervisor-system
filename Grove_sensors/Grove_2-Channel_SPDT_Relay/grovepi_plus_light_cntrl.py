# Turn on/off LED light using top relay of Grove 2 channel relay connected to GrovePi+ port D4
# http://wiki.seeedstudio.com/Grove-2-Channel_SPDT_Relay/

import time
import grovepi

# Connect the Grove 2 ch relay (top relay) to digital port D4
# SIG,NC,VCC,GND
light = 4

grovepi.pinMode(light,"OUTPUT")

while True:
    try:
        # Turn light on for 10 seconds
        grovepi.digitalWrite(light,1)
        print ('start')
        time.sleep(10)

        # Turn off light for 10 seconds and repeat
        grovepi.digitalWrite(light,0)
        print ('stop')
        time.sleep(10)

    except KeyboardInterrupt:
        grovepi.digitalWrite(light,0)
        break
    except IOError:
        print ("Error")
