# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:26:03 2020

@author: jlumpkin
"""

import pandas as pd
from output_report import OutputReport, plot
import numpy as np
from math import sin,cos

num=100
wave=[sin(10*x/num) for x in range(num)]
wave2=[cos(10*x/num) for x in range(num)]
index=[x for x in range(num)]

random=np.random.randint(low = 0, high = 100, size = num)

test=OutputReport(title="Main Title")

plot1=plot(title="Plot 1")
plot1.add_line_graph(wave)
plot1.add_line_graph(wave2,new_graph=False,xlabel="xaxis",ylabel="yaxis")

plot1.add_table([[1,"4","3"],["6",8,"2"]],colLabels=None)


test.add_page(plot1)

plot2=plot(title="Plot 2")
plot2.add_text("fasdofnewofjaoefn\nasfjeoij\n")


test.add_page(plot2)

#test.add_plot(index,wave2)



test.SaveAsPDF()




















