# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:26:03 2020

@author: jlumpkin
"""

import pandas as pd
from output_report import Page
import numpy as np
from math import sin

num=1000
wave=[sin(10*x/num) for x in range(num)]

random=np.random.randint(low = 0, high = 100, size = 1000)

test=Page()








test.show()


test.SaveAsPDF(r"C:\Users\jlumpkin\Desktop\test.pdf")
