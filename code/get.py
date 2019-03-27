# Get data from Grove sensors
# Todd Moore
# 3.17.19

# code that gets values from grove sensors

# ******** WORKING AS OF 3.17.19 *****
#!/usr/bin/env python
# coding=utf-8

import grovepi
import config

def temp():
    try:
        # Get Temperature & Humidity
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp, config.humidity] = grovepi.dht(config.TEMP_SENSOR,config.WHITE) 
        # Convert to Fahrenheit = 9.0/5.0 * Celsius + 32
        config.tempF = (9/5 * temp) + 32
        # print("Temp/Humidity is: ", tempF, humidity)
        # print("get.temp module done")
#        return tempF, humidity

    except IOError:
        print ("Temp/Humid Sensor Error")

def moisture():
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
    try:
        config.moisture = grovepi.analogRead(config.MOISTURE_SENSOR)
        # print("get.moisture module done")
#        return moisture_level

    except IOError:
        print ("Moisture Sensor Error")
            
def air():
    # MQ2 - Combustible Gas, Smoke
    # The sensitivity can be adjusted by the onboard potentiometer
    try:
        # Get Air Quality Value from MQ2 sensor
        # Get sensor value
        sensor_value = grovepi.analogRead(config.GAS_SENSOR)
        # Calculate gas density - large value means more dense gas
        config.density = round((float)(sensor_value / 1024.0)*100, 2)
        # print("sensor_value =", sensor_value, " density =", density)
        # print("get.density done")
#        return density
    
    except IOError:
        print ("Moisture Sensor Error")

# run main() function
if __name__ == "__main__":
    # -------- Test Vectors ------------
    
    temp()
    print("Temp is: ", config.tempF, " F - Humidity is: ", config.humidity,"%")
    moisture()  
    print("Soil Moisture is: ", config.moisture)
    air()   
    print("Density is: ", config.density)
