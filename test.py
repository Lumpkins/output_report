# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:26:03 2020

@author: jlumpkin
"""

import pandas as pd
from output_report import Page, plot
import numpy as np
from math import sin,cos

num=1000
wave=[sin(10*x/num) for x in range(num)]
wave2=[cos(10*x/num) for x in range(num)]
index=[x for x in range(num)]

random=np.random.randint(low = 0, high = 100, size = 1000)

test=Page()

plot1=plot("Turd")
plot1.add_line_graph(wave)
plot1.add_line_graph(wave2,new_graph=False)

test.add_plot(plot1)

plot2=plot("Shart")
plot2.add_scatter_graph(wave,wave2)
test.add_plot(plot2)

#test.add_plot(index,wave2)



test.show()


#test.SaveAsPDF(r"C:\Users\jlumpkin\Desktop\test.pdf")


#import matplotlib.pyplot as plt
#
#
#def annotate_axes(fig):
#    for i, ax in enumerate(fig.axes):
#        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
#        ax.tick_params(labelbottom=False, labelleft=False)
#
#
#fig = plt.figure()
#ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
#ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
#ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
#ax4 = plt.subplot2grid((3, 3), (2, 0))
#ax5 = plt.subplot2grid((3, 3), (2, 1))
#
#annotate_axes(fig)
#
#plt.show()