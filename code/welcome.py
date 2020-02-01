########
# welcome module
# Version: V20-01-27 (This is a working BETA vesion)
# Todd Moore
# 1.27.20
#
# This project is released under The MIT License (MIT)
# Copyright 2020 Todd Moore
########

########
# Code is compatible with Python 2.7 and Python 3.5.
# !/usr/bin/env python
# coding=utf-8
########

########
# python module that displays a startup/welcome routine which lights leds, stdio, & lcd
########

from grovepi import digitalWrite
from grove_rgb_lcd import *
import config
import time
import setup_rpi

def startup():
    # output cool splash screen to stdio
    #    _____ _____   ______          _______ _____ 
    #   / ____|  __ \ / __ \ \        / / ____/ ____|
    #  | |  __| |__) | |  | \ \  /\  / / (___| (___  
    #  | | |_ |  _  /| |  | |\ \/  \/ / \___ \___ \ 
    #  | |__| | | \ \| |__| | \  /\  /  ____) |___) |
    #   \_____|_|  \_\____/   \/  \/  |_____/_____/ 
    #   
    # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ$:$ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ:D?ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ,8~OZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ:88,$ZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZZZOOZZZZZZZZZZZZZZZZZZO?ND8$:ZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZOZZ+:OZZZZZZZZZZZZZZZO7:NDDD:$ZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZZZZ:8~OOZZZZZZZZZZZZZO=:DDD8??ZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZOZZ~8D:ZZZZZZZZZZZZZZO,DDDDDD:ZZZZZZZZZZZZZZZZZZZZZZZZZZ
    # ZZZZZZZ+ID8,:OZZZZZZZZZZZ?8DDDDD8:OZZZZZZZZZZZZZO$:7ZZZZZZZZ
    # ZZZZZZZZ,888O~IZZZZZZZZZZ=,DDDDDN+$ZZZZZZZZZZOO~:8~$ZZZZZZZZ
    # ZZZZZZOZ:O8888,:$OZZZZZZZ+ODDDDD8:ZZZZZZZZZZ$:88DO?ZZZZZZZZZ
    # ZZZZZZZZ~I88888N:IZZZZZZZ:DDDDD8D:ZZOZZZZZI:D8DDD,OZZZZZZZZZ
    # ZZZZZZZZ$~D8DDD88,=ZZZZZZ:ODDDDDD?7ZZZZZ7,O888D8,=OOZZZZZZZZ
    # ZZZZZZZZO?=DDDDD8D,IZZZZZ:DDDDDDD?~ZZZZ::DDDDDD,=ZZZZZZZZZZZ
    # ZZZZZZZZZZI:DDDDDDD:ZOZZZ~DDDDDDD~IZO7:IDDDD88::OZZZZZZZZZZZ
    # ZZZZZZZZZO$:O8DDDDDDD~ZOO,DDDDDDD,ZO~,DDDDDD8=:OOOZZZZZZZZZZ
    # ZZZZZZZZZZZ$,8DDDDDDD::ZZ=ZDD8DDDO7~:NDDDDDD8~OOZZZZZZZZZZZZ
    # ZZZZZZZZZZZZI8DDDDDDND:~Z+8DD8DDD:+:DDD8DDDN:OZZZZZZZZZZZZZZ
    # Z7IZZZZZ$ZZZZ7~DDDDDDDD:Z:,8D8DDD~~DDD8DDNN:ZZZZZZZZZZZZZZZZ
    # $:88I8~,:77Z$Z+~DDDDDDDM:=NDDDDD8::DDDDDD:~$ZZZZZZZZZZZZZZZZ
    # $$:+DD8DDDD,:+ZI~+DDDDDD.:,DDDDDN.NDDDD8:+$Z$$$$$$$$$$$$$$$$
    # $$$I:8DD8DDDDD,:~:=8DDDDD:~D8DD8:NDDD8D:=$$$$$$$$$Z77$$$$$$$
    # $$$$$:,DDDDDD8DDDO:ODDDDDD,:N8DD,DDDND,=$$$I=:,,N$D8887$:::$
    # 777777?:88DDDDDDDDD8ND8D8D:ND8DM8DDNN:I=::?DN8DDDDD8888D+:I7
    # 777777777,$DDDDDDDDDN8+O8DD,D8D+D88,~,Z88DDDD8DNDDDD8::~7777
    # 77777777777:,:DDDDDDD8DN.D8:78?78,::DDDN8DNDDND88D,,?I777777
    # IIIIIIIIIIIII?=:~Z8DNDD8DM$8,8:8::M8DDN8DDDD8N,,:?IIIIIIIIII
    # IIIIIIIIIIIIIII=:,:,~=,DNDDOD88?8DDDDND,=?::=I?IIIIIIIIIIIII
    # IIIIIIIIIIII+:?8DDD8DDDDDD8DDD88888DNDM:,,=?IIIIIIIIIIIIIIII
    # IIIIIII??I~:8DDD8DNNDDDD=,$N8$,DZDNND88DDDNZ,:?I?IIIIIIIIIII
    # ???????I+~N8DDDD8DN8,::,$DDD:8~+DDMZDNDDDDDDDD~:+?I?????????
    # ??????+,NNOD7,,,:~??=:MNDDD,:$+~:NNDM,?NDDDDNNNN8:??????????
    # ???????+???????????~?DNND,:?~O=??:,DDD:=:~:N$DNDD8,+????????
    # ??????????????????+,DI::??????????++:DI=?????++~::,+:???????
    # ???????????????????~?????????????????:?:????????????????????
    # ??????????????????????????????????????~=????????????????????
    # ????????????????????????????????????????????????????????????
    #   _______ _    _ ______                               
    #  |__   __| |  | |  ____|                              
        # | |  | |__| | |__                                 
        # | |  |  __  |  __|                                
        # | |  | |  | | |____                               
    #    _|_|_ |_|__|_|______|         ___                  
    #   / ____|  __ \ / __ \ \        / / |                 
    #  | |  __| |__) | |  | \ \  /\  / /| |__   _____  __   
    #  | | |_ |  _  /| |  | |\ \/  \/ / | '_ \ / _ \ \/ /   
    #  | |__| | | \ \| |__| | \  /\  /  | |_) | (_) >  <    
    #   \_____|_|  \_\____/   \/  \/   |_.__/ \___/_/\_\   
    #   / ____|                           (_)               
    #  | (___  _   _ _ __   ___ _ ____   ___ ___  ___  _ __ 
    #   \___ \| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \| '__|
    #   ____) | |_| | |_) |  __/ |   \ V /| \__ \ (_) | |   
    #  |_____/ \__,_| .__/ \___|_|    \_/ |_|___/\___/|_|   
    #   / ____|     | | | |                                 
    #  | (___  _   _|_|_| |_ ___ _ __ ___                   
    #   \___ \| | | / __| __/ _ \ '_ ` _ \                  
    #   ____) | |_| \__ \ ||  __/ | | | | |                 
    #  |_____/ \__, |___/\__\___|_| |_| |_|                 
            #   __/ |                                       
            #  |___/                                        
    #
    # Verion: 20-01-20-V2B
                                                                    
    # turn on rgb display so user knows GROWSS is not locked up
    setRGB(0,128,0) # display is green
    setText("WELCOM TO GROWSS...")

    # print cool splash screen to stdio
    print("\n\n\n\n\n\n\n\n\n")
    print("   _____ _____   ______          _______ _____ ")
    print("  / ____|  __ \ / __ \ \        / / ____/ ____|")
    print(" | |  __| |__) | |  | \ \  /\  / / (___| (___  ")
    print(" | | |_ |  _  /| |  | |\ \/  \/ / \___ \\___ \ ")
    print(" | |__| | | \ \| |__| | \  /\  / ____) |___) |")
    print("  \_____|_|  \_\\_____/   \/  \/ |_____/_____/ ")
    time.sleep(0.25)
    print("\n")
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ$:$ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ:D?ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ,8~OZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ:88,$ZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZOOZZZZZZZZZZZZZZZZZZO?ND8$:ZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZOZZ+:OZZZZZZZZZZZZZZZO7:NDDD:$ZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZ:8~OOZZZZZZZZZZZZZO=:DDD8??ZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZOZZ~8D:ZZZZZZZZZZZZZZO,DDDDDD:ZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZ+ID8,:OZZZZZZZZZZZ?8DDDDD8:OZZZZZZZZZZZZZO$:7ZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZ,888O~IZZZZZZZZZZ=,DDDDDN+$ZZZZZZZZZZOO~:8~$ZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZOZ:O8888,:$OZZZZZZZ+ODDDDD8:ZZZZZZZZZZ$:88DO?ZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZ~I88888N:IZZZZZZZ:DDDDD8D:ZZOZZZZZI:D8DDD,OZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZ$~D8DDD88,=ZZZZZZ:ODDDDDD?7ZZZZZ7,O888D8,=OOZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZO?=DDDDD8D,IZZZZZ:DDDDDDD?~ZZZZ::DDDDDD,=ZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZZI:DDDDDDD:ZOZZZ~DDDDDDD~IZO7:IDDDD88::OZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZO$:O8DDDDDDD~ZOO,DDDDDDD,ZO~,DDDDDD8=:OOOZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZZZ$,8DDDDDDD::ZZ=ZDD8DDDO7~:NDDDDDD8~OOZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("ZZZZZZZZZZZZI8DDDDDDND:~Z+8DD8DDD:+:DDD8DDDN:OZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("Z7IZZZZZ$ZZZZ7~DDDDDDDD:Z:,8D8DDD~~DDD8DDNN:ZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("$:88I8~,:77Z$Z+~DDDDDDDM:=NDDDDD8::DDDDDD:~$ZZZZZZZZZZZZZZZZ")
    time.sleep(0.25)
    print("$$:+DD8DDDD,:+ZI~+DDDDDD.:,DDDDDN.NDDDD8:+$Z$$$$$$$$$$$$$$$$")
    time.sleep(0.25)
    print("$$$I:8DD8DDDDD,:~:=8DDDDD:~D8DD8:NDDD8D:=$$$$$$$$$Z77$$$$$$$")
    time.sleep(0.25)
    print("$$$$$:,DDDDDD8DDDO:ODDDDDD,:N8DD,DDDND,=$$$I=:,,N$D8887$:::$")
    time.sleep(0.25)
    print("777777?:88DDDDDDDDD8ND8D8D:ND8DM8DDNN:I=::?DN8DDDDD8888D+:I7")
    time.sleep(0.25)
    print("777777777,$DDDDDDDDDN8+O8DD,D8D+D88,~,Z88DDDD8DNDDDD8::~7777")
    time.sleep(0.25)
    print("77777777777:,:DDDDDDD8DN.D8:78?78,::DDDN8DNDDND88D,,?I777777")
    time.sleep(0.25)
    print("IIIIIIIIIIIII?=:~Z8DNDD8DM$8,8:8::M8DDN8DDDD8N,,:?IIIIIIIIII")
    time.sleep(0.25)
    print("IIIIIIIIIIIIIII=:,:,~=,DNDDOD88?8DDDDND,=?::=I?IIIIIIIIIIIII")
    time.sleep(0.25)
    print("IIIIIIIIIIII+:?8DDD8DDDDDD8DDD88888DNDM:,,=?IIIIIIIIIIIIIIII")
    time.sleep(0.25)
    print("IIIIIII??I~:8DDD8DNNDDDD=,$N8$,DZDNND88DDDNZ,:?I?IIIIIIIIIII")
    time.sleep(0.25)
    print("???????I+~N8DDDD8DN8,::,$DDD:8~+DDMZDNDDDDDDDD~:+?I?????????")
    time.sleep(0.25)
    print("??????+,NNOD7,,,:~??=:MNDDD,:$+~:NNDM,?NDDDDNNNN8:??????????")
    time.sleep(0.25)
    print("???????+???????????~?DNND,:?~O=??:,DDD:=:~:N$DNDD8,+????????")
    time.sleep(0.25)
    print("??????????????????+,DI::??????????++:DI=?????++~::,+:???????")
    time.sleep(0.25)
    print("???????????????????~?????????????????:?:????????????????????")
    time.sleep(0.25)
    print("??????????????????????????????????????~=????????????????????")
    time.sleep(0.25)
    print("????????????????????????????????????????????????????????????")
    time.sleep(0.25)
    print("")
    time.sleep(0.25)
    print("  _______ _    _ ______                               ")
    time.sleep(0.25)
    print(" |__   __| |  | |  ____|                              ")
    time.sleep(0.25)
    print("    | |  | |__| | |__                                 ")
    time.sleep(0.25)
    print("    | |  |  __  |  __|                                ")
    time.sleep(0.25)
    print("    | |  | |  | | |____                               ")
    time.sleep(0.25)
    print("   _|_|_ |_|__|_|______|         ___                  ")
    time.sleep(0.25)
    print("  / ____|  __ \ / __ \ \        / / |                 ")
    time.sleep(0.25)
    print(" | |  __| |__) | |  | \ \  /\  / /| |__   _____  __   ")
    time.sleep(0.25)
    print(" | | |_ |  _  /| |  | |\ \/  \/ / | '_ \ / _ \ \/ /   ")
    time.sleep(0.25)
    print(" | |__| | | \ \| |__| | \  /\  /  | |_) | (_) >  <    ")
    time.sleep(0.25)
    print("  \_____|_|  \_\\____/   \/  \/   |_.__/ \___/_/\_\   ")
    time.sleep(0.25)
    print("  / ____|                           (_)               ")
    time.sleep(0.25)
    print(" | (___  _   _ _ __   ___ _ ____   ___ ___  ___  _ __ ")
    time.sleep(0.25)
    print("  \___ \| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \| '__|")
    time.sleep(0.25)
    print("  ____) | |_| | |_) |  __/ |   \ V /| \__ \ (_) | |   ")
    time.sleep(0.25)
    print(" |_____/ \__,_| .__/ \___|_|    \_/ |_|___/\___/|_|   ")
    time.sleep(0.25)
    print("  / ____|     | | | |                                 ")
    time.sleep(0.25)
    print(" | (___  _   _|_|_| |_ ___ _ __ ___                   ")
    time.sleep(0.25)
    print("  \___ \| | | / __| __/ _ \ '_ ` _ \                  ")
    time.sleep(0.25)
    print("  ____) | |_| \__ \ ||  __/ | | | | |                 ")
    time.sleep(0.25)
    print(" |_____/ \__, |___/\__\___|_| |_| |_|                 ")
    time.sleep(0.25)
    print("          __/ |                                       ")
    time.sleep(0.25)
    print("         |___/                                        ")
    time.sleep(0.25)
    print("\nVERSION: " + config.RPIENVCONTRLR_VER + " \n\n")
    # ---------------------------------------------------------------------------------------
    # turn on LEDs
    setText("GROWSS IS\n" + "STARTING...")
    digitalWrite(config.TEMP_ALARM_LED, 1)     # turn on temp alarm led on RPI
    digitalWrite(config.HUMID_ALARM_LED, 1)     # turn on humidity alarm led     
    digitalWrite(config.MOISTURE_ALARM_LED, 1)     # Turn on soil moisture LED
    digitalWrite(config.MOISTURE2_ALARM_LED, 1)     # Turn on soil moisture2 LED       
    digitalWrite(config.ATOMIZER_ON_LED, 1)     # Turn on atomizer LED       

    # ---------------------------------------------------------------------------------------
    # iterate through different RGB colors on LCD dsiplay
    time.sleep(0.25)
    setRGB(0,0,0) # display is black
    time.sleep(0.25)
    setRGB(255,0,0) # display is red
    setText("TEMP ALARM LED")
    digitalWrite(config.TEMP_ALARM_LED, 0)     # turn off temp alarm led
    time.sleep(0.25)
    setRGB(0,255,0) # display is lime
    time.sleep(0.25)
    setRGB(0,0,255) # display is blue
    time.sleep(0.25)
    setText("HUMID ALARM LED")
    digitalWrite(config.HUMID_ALARM_LED, 0)     # turn off humidity alarm led     
    setRGB(255,255,0) # display is yellow
    time.sleep(0.25)
    setRGB(0,255,255) # display is cyan
    time.sleep(0.25)
    setRGB(255,0,255) # display is magenta
    time.sleep(0.25)
    setRGB(192,192,192) # display is silver
    time.sleep(0.25)
    setText("MOIST ALARM LED")
    digitalWrite(config.MOISTURE_ALARM_LED, 0)  # Turn off soil moisture LED
    setRGB(128,128,128) # display is grey
    time.sleep(0.25)
    setRGB(128,0,0) # display is maroon
    time.sleep(0.25)
    setRGB(128,128,0) # display is olive
    time.sleep(0.25)
    setRGB(0,128,0) # display is green
    time.sleep(0.25)
    setText("MOIST2 ALARM LED")
    digitalWrite(config.MOISTURE2_ALARM_LED, 0)     # Turn off smoke LED       
    setRGB(128,0,128) # display is purple
    time.sleep(0.25)
    setRGB(0,128,128) # display is teal
    time.sleep(0.25)
    setRGB(0,0,128) # display is navy
    time.sleep(0.25)
    setText("ATOM ALARM LED")
    digitalWrite(config.ATOMIZER_ON_LED, 0)     # Turn off atomizer LED       
    setRGB(255,255,255) # display is white
    time.sleep(0.25)

	# ---------------------------------------------------------------------------------------
    # turn off/on exhaust fan (exhaust fan is already on by default)
    setText("FAN OFF/ON")
    digitalWrite(config.FAN, 1)     # turn off exhaust fan        
    time.sleep(1)
    digitalWrite(config.FAN, 0)     # turn on exhaust fan        
    time.sleep(1)
    digitalWrite(config.FAN, 1)     # turn off exhaust fan        
	
    # turn on/off light
    setText("LIGHT ON/OFF")
    digitalWrite(config.LIGHT, 1)     # turn off grow light
    time.sleep(1)
    digitalWrite(config.LIGHT, 0)     # turn on grow light
    time.sleep(1)
    digitalWrite(config.LIGHT, 1)     # turn off grow light

    # turn on/off buzzer
    setText("BUZZER ON/OFF")
    digitalWrite(config.BUZZER, 1)     # turn on buzzer
    time.sleep(0.5)
    digitalWrite(config.BUZZER, 0)     # turn off buzzer

    # turn on/off atomizer
    setText("ATOMIZER ON/OFF")
    digitalWrite(config.ATOMIZER, 1)     # turn on atomizer 
    time.sleep(1)
    digitalWrite(config.ATOMIZER, 0)     # turn off atomizer 
    setRGB(0,0,0) # display is black


# run main() function
if __name__ == "__main__":
    # Setup Hardware
    setup_rpi.hardware()
    startup()
