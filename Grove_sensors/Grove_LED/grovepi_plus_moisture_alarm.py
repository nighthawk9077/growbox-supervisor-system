# Turn on/off Soil Moisture Alarm LED connected to GrovePi+ port D8
# I'll be using my own LEDs instead of the Grove LEDs.  However, I'm using the code, grove_led_blink.py,
# to drive the led from here:
# http://wiki.seeedstudio.com/Grove-Red_LED/

# Connect Temperature Alarm LED to digital port D7
moisture_alarm_led = 8

pinMode(moisture_alarm_led,"OUTPUT")
time.sleep(1)

print ("This example will blink an LED connected to the GrovePi+ on the port labeled D8. If you're having trouble seeing the LED blink, be sure to check the LED connection and the port number. You may also try reversing the direction of the LED on the sensor.")
print (" ")
print ("Connect the LED to the port labele D8!" )

while True:
    try:
        #Blink the LED
        digitalWrite(moisture_alarm_led,1)     # Send HIGH to switch on LED
        print ("LED ON!")
        time.sleep(1)

        digitalWrite(moisture_alarm_led,0)     # Send LOW to switch off LED
        print ("LED OFF!")
        time.sleep(1)

    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(moisture_alarm_led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print ("Error")
