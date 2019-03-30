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
	server = smtplib.SMTP('smtp.gmail.com', 587)

	#Next, log in to the server
	server.login("youremailusername", "password")

#Send the mail
msg = "
Hello!" # The /n separates the message from the headers
server.sendmail("you@gmail.com", "target@example.com", msg)

# run main() function
if __name__ == "__main__":
    startup()
   