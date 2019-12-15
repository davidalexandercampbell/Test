# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:04:13 2019

@author: david
"""

# sine wave

import numpy as np
import matplotlib.pyplot as plt

y = np.pi

values = np.arange(-y,y,y/16)
x1 = np.sin(values)
x2 = np.cos(values)



figure =plt.figure()
plt.plot(values,x1,values,x2)
#plt.show()

#add some new code