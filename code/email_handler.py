########
# email handler module
# Version: 2019-03-27V1A (This is an alpha version & not yet complete
# Todd Moore
# 3.29.19
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
# python module that sends an email alert if there is an alarm present
########

import smtplib
import config
import time

def send():
    # ---------------------------------------------------------------------------------------
    # The first step is to create an SMTP object, each object is used for connection 
    # with one server.
    server = smtplib.SMTP(config.growss_email_server, config.growss_email_port)
    
    # indicate to smtp server to use the extended smtp protocol
    server.ehlo()

    # turn on tls service on server
    server.starttls()

    #Next, log in to the server
    server.login(config.growss_email_addr, config.growss_email_pwd)
    
    #Send the mail
    # if there is a temp alarm...
    if (config.temp_alarm == "ON"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS TEMP ALARM!!!"
        TEXT = "YOUR GROWSS HAS A TEMPERATURE ALARM!!!! \
                TEMPERATURE IS " + str(config.tempF) + " F Degrees"
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
    
    if (config.humid_alarm == "ON"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS HUMIDITY ALARM!!!"
        TEXT = "YOUR GROWSS HAS A HUMIDITY ALARM!!!! \
                HUMIDITY IS " + str(config.humidity) + " %"
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
    
    if (config.moisture_alarm != "PERFECT"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS SOIL MOISTURE ALARM!!!"
        TEXT = "YOUR GROWSS HAS A SOIL MOISTURE ALARM!!!! \
                SOIL MOISTURE IS " + config.moisture_alarm
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
    
    if (config.smoke_alarm == "ON"):
        # The /n separates the message from the headers"
        SUBJECT = "GROWSS SMOKE ALARM!!!"
        TEXT = "YOUR GROWSS HAS A SMOKE ALARM!!!! \
                DENSITY IS " + str(config.density) + " %"
        msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail(config.growss_email_addr, config.growss_email_sender_addr, msg)
    server.close()

# run main() function
if __name__ == "__main__":
    config.temp_alarm = "OFF"
    config.humid_alarm = "OFF"
    config.moisture_alarm = "PERFECT"
    config.smoke_alarm = "OFF"
    send()
   