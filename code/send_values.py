########
# sends values to various outputs
# Version: 19-04-25-V1B (This is a working BETA vesion)
# Todd Moore
# 5.20.19
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# # Code is compatible with Python 2.7 and Python 3.5.
#!/usr/bin/env python
# coding=utf-8
########

########
# send values to various outputs, like file, RGB LCD, & STDIO
########

from grove_rgb_lcd import *
import time
import datetime
import config

def save_to_file():

    # Values will be added as tab seperated delimited data with the following format:
    # datetime  temp    hi temp alarm   low temp alarm  temp_alarm  hi temp value   low temp value
    # humidity  hi humidity alarm   low humidity alarm  humidity alarm  hi humidity value
    # lo humidity value moisture  hi moisture alarm   low moisture alarm  moisture alarm  
    # hi moisture value lo moisture value   density   hi density alarm    hi density value    
    # lo density value  smoke alarm   fan on  ataomizer on

    # a new file is saved every day
    fmt ='%Y-%m-%d'
    date_str = datetime.datetime.now().strftime(fmt)

    filename = config.RetValFolder + date_str + "_" + config.fname_log
    
    # concatenate data into 1 string argument
    values = config.DATA_TIME + "\t" + \
                str(config.tempF) + "\t" + \
                str(config.HI_TEMP_ALARM) + "\t" + \
                str(config.LO_TEMP_ALARM) + "\t" + \
                config.temp_alarm + "\t" + \
                str(config.hi_temp_value) + "\t" + \
                str(config.lo_temp_value) + "\t" + \
                str(config.humidity) + "\t" + \
                str(config.HI_HUMID_ALARM) + "\t" + \
                str(config.LO_HUMID_ALARM) + "\t" + \
                config.humid_alarm + "\t" + \
                str(config.hi_humid_value) + "\t" + \
                str(config.lo_humid_value) + "\t" + \
                str(config.moisture) + "\t" + \
                config.moisture_alarm + "\t" + \
                str(config.hi_moisture_value) + "\t" + \
                str(config.lo_moisture_value) + "\t" + \
                str(config.density) + "\t" + \
                str(config.HI_DENSITY_ALARM) + "\t" + \
                str(config.hi_density_value) + "\t" + \
                str(config.lo_density_value) + "\t" + \
                config.smoke_alarm + "\t" + \
                config.fan_on + "\t" + \
                str(config.FAN_ON_HUMID) + "\t" + \
                str(config.FAN_ON_TEMP) + "\t" + \
                config.atomizer_on + "\t" + \
                str(config.ATOMIZER_HI_HUMIDITY) + "\n"

    print("Values being saved to file " + filename + ":" )
    print(values)

    # appends the values, then automatically closes the file for me
    with open(filename, "a") as myfile: 
        myfile.writelines(values)

# ---------------------------------------------------------------------------------------
def print_to_stdio():

    # STDIO format is:
    #
    # Date/Time:    05/17/2019 05:27:00 
    #----------------------------------------------------------------------------------
    # temp alarm    OFF     humid alarm OFF     moisture alarm  PERFECT smoke_alarm OFF
    # temp          70.0 F  humidity    70%     moisture        500     density     800
    # hi temp       75.0 F  hi humid    75%     hi moisture     500     hi density  900
    # lo temp       65.0 F  lo humid    62%     lo moisture     400     lo density  875
    # hi alarm      80 F    hi alarm    80%                             hi alarm    1000
    # low alarm     65 F    low alarm   60%                              
    #                    
    # fan on        OFF     atomizer on OFF  
    # fan hi temp   75 F    atomizer
    # fan hi humid  85 F    low humid   25%

    print("Date/Time    " + config.DATA_TIME)
    print("-----------------------------------------------------------------------------------------")
    print("temp alarm \t" + config.temp_alarm + "\t" + "humid alarm \t" + config.humid_alarm + "\t" 
        + "moisture alarm \t" + config.moisture_alarm + "\t" + "smoke alarm \t" + config.smoke_alarm)

    print("temp \t" + "\t" + str(config.tempF) + " F\t" + "humidity \t" + str(config.humidity) + " %\t" 
        + "moisture \t" + str(config.moisture) + "\t" + "density \t" + str(config.density))

    print("hi alarm \t" + str(config.HI_TEMP_ALARM) + " F\t" + "hi alarm \t" + str(config.HI_HUMID_ALARM) 
        + " %\t\t\t\t" + "hi alarm \t" + str(config.HI_DENSITY_ALARM))

    print("low alarm \t" + str(config.LO_TEMP_ALARM) + " F\t" + "low alarm \t" + str(config.LO_HUMID_ALARM) 
        + " %")

    print("hi temp \t" + str(config.hi_temp_value) + " F\t" + "hi humid \t" + str(config.hi_humid_value) 
        + " %\t" + "hi moisture \t" + str(config.hi_moisture_value) + "\thi density \t" 
        + str(config.hi_density_value))

    print("lo temp \t" + str(config.lo_temp_value) + " F\t" + "lo humid \t" + str(config.lo_humid_value) 
        + " %\t"+ "lo moisture \t" + str(config.lo_moisture_value) + "\tlo density \t" 
        + str(config.lo_density_value))
    print("")
    print("fan on \t\t" + config.fan_on + "\t" + "atomizer on \t" + config.atomizer_on)
    print("fan on temp \t" + str(config.FAN_ON_TEMP) + " F\t" + "atomizer")
    print("fan hi humid \t" + str(config.FAN_ON_HUMID) + " %\t" + "hi humid \t" 
        + str(config.ATOMIZER_HI_HUMIDITY) + " %")

def version_to_lcd():
    # display version & author info on startup
    setRGB(0,128,128) # display is teal
    setText(config.RPIENVCONTRLR_NAME1 + "\n" + config.RPIENVCONTRLR_NAME2)
    time.sleep(1)
    setText(config.RPIENVCONTRLR_NAME3 + "\n" + config.RPIENVCONTRLR_NAME4)
    time.sleep(1)
    setText("Version #:\n" + config.RPIENVCONTRLR_VER) 
    time.sleep(1)
    setText("Author:\n" + config.RPIENVCONTRLR_AUTH)
    time.sleep(1)
    setText("License:\n" + config.RPIENVCONTRLR_LIC)
    time.sleep(1)

def print_to_LCD():
 #   Display Environmental Data on LCD Screen
    setRGB(0,153,0) # display is green
    setText("Date/Time:\n" + config.DATA_TIME)
    time.sleep(1)

    if (config.temp_alarm == "ON"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Temp: " + str(config.tempF) + " F\nAlarm: " + config.temp_alarm)
    time.sleep(1)
    
    setRGB(0,153,0) # display is green
    setText("Hi Temp: " + str(config.hi_temp_value) + " F\nLo Temp: " + str(config.lo_temp_value) + " F")
    time.sleep(1)

    if (config.humid_alarm == "ON"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    setText("Humidity: " + str(config.humidity) + " %\nAlarm: " + config.humid_alarm)
    time.sleep(1)  

    setRGB(0,153,0) # display is green
    setText("Hi Humid: " + str(config.hi_humid_value) + " %\nHumid Hyst: " + str(config.FAN_HUMID_HYSTERESIS) + " %")
    time.sleep(1)
    
    if (config.moisture_alarm == "AIR"):
        setRGB(204,102,0) # display is orange
    elif (config.moisture_alarm == "DRY"):
        setRGB(204,204,0) # display is yellow
    elif (config.moisture_alarm == "PERFECT"):
        setRGB(0,153,0) # display is green
    elif (config.moisture_alarm == "WATER"):
        setRGB(0,0,204) # display is dark blue
    else:
        setRGB(255,0,0) # alarm - display is red
    setText("Moisture: " + str(config.moisture) + "\nAlarm: " + config.moisture_alarm)
    time.sleep(1)
    
    setRGB(0,153,0) # display is green
    setText("Hi Moist: " + str(config.hi_moisture_value) + "\nLo Moist: " + str(config.lo_moisture_value))
    time.sleep(1)

    if (config.smoke_alarm == "ON"):
        setRGB(255,0,0) # alarm - display is red
    else:
        setRGB(0,153,0) # no, alarm - display is green
    
    setText("Density is " + str(config.density) + "\nAlarm: " + config.smoke_alarm)
    time.sleep(1)

    setRGB(0,153,0) # display is green
    setText("Hi Dens: " + str(config.hi_density_value) + "\nLo Dens: " + str(config.lo_density_value))
    time.sleep(1)

    setText("Fan is " + config.fan_on)
    time.sleep(1)

    setText("Fan On Temp:\n" + str(config.FAN_ON_TEMP) + " F")
    time.sleep(1)

    setText("Fan On Hi Humid:\n" + str(config.FAN_ON_HUMID) + " %")
    time.sleep(1)

    setText("Atomizer is " + config.atomizer_on + "\n") 
    time.sleep(1)
 
    setText("Atom On Hi Hum:\n" + str(config.ATOMIZER_HI_HUMIDITY) + " %")
    time.sleep(1)


# run main() function
if __name__ == "__main__":
    import datetime
    # -------- Test Vectors ------------
    data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Data Date/Time is ", data_time)

    save_to_file(data_time)

    print_to_stdio(data_time)

    print_to_LCD(data_time)
