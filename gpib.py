# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:56:27 2019

@author: david
"""

#gpib


import pyvisa as visa

rm = visa.ResourceManager('@sim')
print(rm.list_resources())