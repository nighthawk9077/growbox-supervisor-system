########
# email handler module
# Version: V20-01-27 (This is a working BETA vesion)
# Todd Moore
# 1.27.20
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# Code is compatible with Python 2.7 and Python 3.5.
# !/usr/bin/env python
# coding=utf-8
########

########
# python module that sends an email &/or text alert if there is an alarm present
########

import smtplib
import config
import time


def send():
    # create an SMTP object, each object is used for connection 
    # with one server.
    server = smtplib.SMTP(config.growss_email_server, config.growss_email_port)

    # indicate to smtp server to use the extended smtp protocol
    server.ehlo()

    # turn on tls service on server
    server.starttls()

    #log in to the server
    server.login(config.growss_email_addr, config.growss_email_pwd)
    #__________________________________________________________________________________

    #Send the mail
    # if there is a temp alarm...
    if (config.temp_alarm == "ON"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS TEMP ALARM!!!"
        TEXT = "YOUR GROWSS HAS A TEMPERATURE ALARM!!!!\n" \
                + "TEMPERATURE IS " + str(config.bme280_tempF) + " F"
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
        # Send text message through SMS gateway of destination number

    # if there is a humidity alarm...
    if (config.humid_alarm == "ON"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS HUMIDITY ALARM!!!"
        TEXT = "YOUR GROWSS HAS A HUMIDITY ALARM!!!!\n" \
                + "HUMIDITY IS " + str(config.bme280_humidity) + " %"
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
    
    # if there is a soil moisture alarm...
    if (config.moisture_alarm != "PERFECT"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS SOIL MOISTURE ALARM!!!"
        TEXT = "YOUR GROWSS HAS A SOIL MOISTURE ALARM!!!!\n" \
                + "SOIL MOISTURE 1 & 2 IS " + config.moisture, config.moisture2
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
    
    server.close()

# run main() function
if __name__ == "__main__":
    config.temp_alarm = "ON"
    config.humid_alarm = "OFF"
    config.moisture_alarm = "AIR"
    send()
   