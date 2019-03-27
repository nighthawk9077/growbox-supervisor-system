# Output sound through Grove Piezo Buzzer connected to GrovePi+ port D0
# http://wiki.seeedstudio.com/Grove-Buzzer/

import time
import grovepi

# Connect the Grove Buzzer to digital port D0
# SIG,NC,VCC,GND
buzzer = 0

grovepi.pinMode(buzzer,"OUTPUT")

while True:
    try:
        # Buzz for 1 second
        grovepi.digitalWrite(buzzer,1)
        print ('start')
        time.sleep(1)

        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer,0)
        print ('stop')
        time.sleep(1)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")
