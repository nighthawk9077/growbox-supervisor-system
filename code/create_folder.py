########
# create folder
# Version: 2019-04-25V1B
# Todd Moore
# 5.9.19
#
# This project is released under The MIT License (MIT)
# Copyright 2019 Todd Moore
########

########
# Code is compatible with Python 2.7 and Python 3.5.
#!/usr/bin/env python
# coding=utf-8
########

########
# create a folder if none exists
########
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
