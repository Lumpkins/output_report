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

test=OutputReport()

plot1=plot(title="Plot 1")
plot1.add_line_graph(wave)
plot1.add_line_graph(wave2,new_graph=False,xlabel="xaxis",ylabel="yaxis")



test.add_text("This is the title",type="title")
test.add_text("plot 1:",type="heading")
test.add_plot(plot1)
test.add_text("\tOk, well that was the plot, YAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")


table_data=pd.DataFrame.from_csv(r"C:\Users\jlumpkin\Desktop\data\ff.csv")


test.add_table(table_data,title="Tabular Data Bruh")
#plot2=plot(title="Plot 2")
#plot2.add_text("fasdofnewofjaoefn\nasfjeoij\n")



#test.add_page(plot2)



#test.add_plot(index,wave2)



test.Save()




















