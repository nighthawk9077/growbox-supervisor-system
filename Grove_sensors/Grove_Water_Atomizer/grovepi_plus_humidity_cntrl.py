# Turn on/off water atomizer connected to GrovePi+ to port D3
# http://wiki.seeedstudio.com/Grove-Water_Atomization/

import time
import grovepi

# Connect the Grove Water Atomizer to port D3
# SIG,NC,VCC,GND
atomizer = 3

grovepi.pinMode(atomizer,"OUTPUT")

while True:
    try:
        # Turn atomizer on for 10 seconds
        grovepi.digitalWrite(atomizer,1)
        print ('start')
        time.sleep(10)

        # Turn off atomizer for 10 seconds and repeat
        grovepi.digitalWrite(atomizer,0)
        print ('stop')
        time.sleep(10)

    except KeyboardInterrupt:
        grovepi.digitalWrite(atomizer,0)
        break
    except IOError:
        print ("Error")
