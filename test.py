# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:26:03 2020

@author: jlumpkin
"""

import pandas as pd
from output_report import OutputReport, plot
import numpy as np
from math import sin,cos

num=1000
wave=[sin(10*x/num) for x in range(num)]
wave2=[cos(10*x/num) for x in range(num)]
index=[x for x in range(num)]

random=np.random.randint(low = 0, high = 100, size = 1000)

test=OutputReport(title="My name is Wade")

plot1=plot(title="Turd")
plot1.add_line_graph(wave)
plot1.add_line_graph(wave2,new_graph=False)

test.add_page(plot1)

plot2=plot(title="Shart")
plot2.add_scatter_graph(wave,wave2)
test.add_page(plot2)

#test.add_plot(index,wave2)



test.SaveAsPDF()


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









# import datetime
# import numpy as np
# from matplotlib.backends.backend_pdf import PdfPages
# import matplotlib.pyplot as plt
# import os
# # Create the PdfPages object to which we will save the pages:
# # The with statement makes sure that the PdfPages object is closed properly at
# # the end of the block, even if an Exception occurs.
# loc=r'C:\Users\jlumpkin\Desktop\multipage_pdf.pdf'
# with PdfPages(loc) as pdf:
#     plt.figure(figsize=(8.5, 11))
#     plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
#     plt.title('Page One')
#     pdf.savefig()  # saves the current figure into a pdf page
#     plt.close()

#     # if LaTeX is not installed or error caught, change to `usetex=False`
#     plt.rc('text', usetex=False)
#     plt.figure(figsize=(8, 6))
#     x = np.arange(0, 5, 0.1)
#     plt.plot(x, np.sin(x), 'b-')
#     plt.title('Page Two')
#     pdf.attach_note("plot of sin(x)")  # you can add a pdf note to
#                                        # attach metadata to a page
#     pdf.savefig()
#     plt.close()

#     plt.rc('text', usetex=False)
#     fig = plt.figure(figsize=(4, 5))
#     plt.plot(x, x ** 2, 'ko')
#     plt.title('Page Three')
#     pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
#     plt.close()

#     # We can also set the file's metadata via the PdfPages object:
#     d = pdf.infodict()
#     d['Title'] = 'Multipage PDF Example'
#     d['Author'] = 'Jouni K. Sepp\xe4nen'
#     d['Subject'] = 'How to create a multipage pdf file and set its metadata'
#     d['Keywords'] = 'PdfPages multipage keywords author title subject'
#     d['CreationDate'] = datetime.datetime(2009, 11, 13)
#     d['ModDate'] = datetime.datetime.today()


# os.startfile(loc)
























