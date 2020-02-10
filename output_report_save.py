import sys

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from plot_params import ePlot_type
import pandas as pd
import os



class OutputReport():

    def __init__(self,**kwargs):
        self.title=kwargs.get("title",None)
        self.loc=kwargs.get("loc",r"C:\test.pdf")

        self.file=PdfPages(self.loc)

    def add_page(self,plots):#may intake multiple plot objects, page will scale acrordingly
        if not isinstance(plots,list):
            plots=[plots]
        
        for plot in plots:
<<<<<<< HEAD
            if not plot.generated:
                plot.generate_plot()
=======
            plot.generate_plot()
>>>>>>> d07b815db2f760e57cad1242374929c3ddb197b9
            self.file.savefig(plot.figure)



<<<<<<< HEAD
    def SaveAsPDF(self):
=======



    def SaveAsPDF(self,show=True):
>>>>>>> d07b815db2f760e57cad1242374929c3ddb197b9
        self.file.close()
        os.startfile(self.loc)
 





class plot():
    """
Data : list (x and y), Series or Dataframe objects

kwargs:
    start_date
    
    end_date
    
    title=""
    
    ylabel=False
    
    xlabel=False
    
    width=1
    
    sharex=False, share x axis with previous plot
    
    sharey=False, share y axis with previous plot
    
    new_graph, default of True, set to False if you want the current Data to be
    plotted on the current subplot
    
    new_line, default = True, set to False if you want the current addition to
    be added horizontally on the report, ei for the graphs to be side by side
    instead of below the previous graph


https://www.python-course.eu/matplotlib_multiple_figures.php


@author: jlumpkin
"""
    def __init__(self,**kwargs):
        plt.rcParams.update({'figure.max_open_warning': 0})
        self._initialize_variables()
        
        self.title=kwargs.get("title","")
        self.figsize=kwargs.get("figsize",(8.5,11))
      
        self.figure=None
        self.generated=False

    def generate_plot(self):
            plt.ioff()
            
            #plt.style.use('dark_background')
            plt.style.use('default')
            
            self.nrow=self.current_row+self._height_save
            
            prev_ax=None
            tolerance = 10 # points
            connected=False
<<<<<<< HEAD
            figure, ax=plt.subplots(figsize=self.figsize)
=======
            figure, ax=plt.subplots(figsize=self.figsize)#figsize=(2*self.ncol+1,2*self.nrow+1))
>>>>>>> d07b815db2f760e57cad1242374929c3ddb197b9
            
            self.figure=figure
            
            gridsize = ( self.nrow,self.ncol)
            plt.rcParams['axes.axisbelow'] = True
            for plot in self.plots:
                
                
                if plot["New Graph"]:
                    if  plot["sharex"]:
    
                        prev_ax=plt.subplot2grid(gridsize,(plot["Row"]-1,plot["Col"]-1),rowspan=plot["height"],colspan=plot["width"],sharex=prev_ax)
                        plt.setp(prev_ax.get_xticklabels(), visible=False)
                    elif plot["sharey"]:
    
                        prev_ax=plt.subplot2grid(gridsize,(plot["Row"]-1,plot["Col"]-1),rowspan=plot["height"],colspan=plot["width"],sharey=prev_ax)
                        plt.setp(prev_ax.get_yticklabels(), visible=False)
                    else:
    
                        prev_ax=plt.subplot2grid(gridsize,(plot["Row"]-1,plot["Col"]-1),rowspan=plot["height"],colspan=plot["width"])
                    plt.grid(True, linewidth=1)

                    
                if plot["plot_title"]:
                    prev_ax.set_title(plot["plot_title"])
                if plot["xlabel"]:
                    prev_ax.set_xlabel(plot["Data"].index.name)
                if plot["ylabel"]:
                    prev_ax.set_ylabel(plot["Data"].name)
                
                #pdb.set_trace()
                if plot["Type"]==ePlot_type.line:
    
                    prev_ax.plot(plot["Data"],color=plot["color"], picker=tolerance)
                elif plot["Type"]==ePlot_type.scatter:
    
                    prev_ax.scatter(plot["Data"].index,plot["Data"].values,s=plot["s"],color=plot["color"],marker=plot["marker"], picker=tolerance)         
                elif plot["Type"]==ePlot_type.histogram:
                    prev_ax.hist(plot["Data"],bins=plot["bin"], picker=tolerance)     
                elif plot["Type"]==ePlot_type.span:
                    for span in plot["Data"]:
                        prev_ax.axvspan(span[0],span[1], color=plot["color"],alpha=.5)
                elif plot["Type"]==ePlot_type.table:
                    prev_ax.table(cellText=plot["Data"],rowLabels=plot["rowLabels"],colLabels=plot["colLabels"])
                    prev_ax.axis("off")
                
                if plot["create_legend"]:
                    plt.legend(loc='best')
                if plot["func"] and not connected:
                    figure.func=plot["func"]
                    
                    connected=True
                    
               
                #plt.tight_layout()
                
                #plt.subplots_adjust(hspace=1)
                
                if plot["figure_title"]:
                    #print(plot["figure_title"])
                    plt.suptitle(plot["figure_title"])


            self._initialize_variables()

            self.generated=True

    def plot_dict(self,**kwargs):
        plot={"Data":kwargs.get("Data",None),
            "New Graph":kwargs.get("new_graph",True),
            "Type":kwargs.get("Type",None),
            "Row":self.current_row,
            "Col":self.current_col,
            "plot_title":kwargs.get("plot_title",False),
            "figure_title":kwargs.get("figure_title",False),
            "xlabel":kwargs.get("xlabel",False),
            "ylabel":kwargs.get("ylabel",False),
            "width":kwargs.get("width",1),
            "height":kwargs.get("height",2),
            "sharex":kwargs.get("sharex",False),
            "sharey":kwargs.get("sharey",False),
            "create_legend":kwargs.get("create_legend",False),
            "func":kwargs.get("func",None)}

        
        return plot


    def add_spans(self,Data,**kwargs):
        #Data must be a list of tuples with (start_date, end_date)

        self._adjust_plot_pos(**kwargs)

        plot=self.plot_dict(Data=Data,Type=ePlot_type.span,**kwargs)
        
        plot["color"]=kwargs.get("color","green")
        
        if plot["height"]>self._height_save:
            self._height_save=plot["height"]

        self.plots.append(plot)


    
    def add_line_graph(self,*Data,**kwargs):


        Data=self._santize_data(*Data)

        self._adjust_plot_pos(**kwargs)

        plot=self.plot_dict(Data=Data,Type=ePlot_type.line,**kwargs)
        
        plot["color"]=kwargs.get("color","red")
        
        if plot["height"]>self._height_save:
            self._height_save=plot["height"]

        self.plots.append(plot)


            
            
    def add_scatter_graph(self,*Data,**kwargs):

        Data=self._santize_data(*Data)

        self._adjust_plot_pos(**kwargs)
        
        plot=self.plot_dict(Data=Data,Type=ePlot_type.scatter,**kwargs)

        plot["color"]=kwargs.get("color","red")
        plot["s"]=kwargs.get("s",3)
        plot["marker"]=kwargs.get("marker","o")#https://matplotlib.org/api/markers_api.html

        
        if plot["height"]>self._height_save:
            self._height_save=plot["height"]

        self.plots.append(plot)     


    def add_histogram_graph(self,*Data,**kwargs):

        Data=self._santize_data(*Data)

        self._adjust_plot_pos(**kwargs)

        plot=self.plot_dict(Data=Data,Type=ePlot_type.histogram,**kwargs)

        plot["bin"]=kwargs.get("bin",6)#this keyword applies to histograms only
        
        if plot["height"]>self._height_save:
            self._height_save=plot["height"]

        self.plots.append(plot) 

    def add_table(self,Data,**kwargs):#Data must be list or list of lists

        
        self._adjust_plot_pos(**kwargs)

        plot=self.plot_dict(Data=Data,Type=ePlot_type.table,**kwargs)

        plot["rowLabels"]=kwargs.get("rowLabels",[x for x in range(len(Data))])
        max_col_length=0
        for col in Data:
            if len(col)>max_col_length:
                max_col_length=len(col)
        plot["colLabels"]=kwargs.get("colLabels",[x for x in range(max_col_length)])


        if plot["height"]>self._height_save:
            self._height_save=plot["height"]

        self.plots.append(plot)         


            
    def _initialize_variables(self):
        self.nrow, self.ncol, self.current_row, self.current_col =1,1,1,1
        self._height_save=1
        self.plots=list()#list of dicts
        
        self.first_plot=True
        
    def _adjust_plot_pos(self,**kwargs):
        if self.first_plot:
            self.first_plot=False
            self.nrow+=kwargs.get("height",1)-1
            return
        new_graph=kwargs.get("new_graph",True)
        
        if new_graph:

            new_line=kwargs.get("new_line",True)
            
            
            if new_line:#if this addition is stacking vertically
                self.current_col=1
                self.current_row+=self._height_save
                self.nrow+=self._height_save
                self._height_save=1
            else:#if this addition if stacking horizontally
                self.current_col+=1
                if self.current_col>self.ncol:
                    self.ncol+=1
                    

                
                
    def _santize_data(self,*Data):#insures data become a Series object

        if len(Data)==1  :
            if isinstance(Data[0],pd.Series) or isinstance(Data[0],pd.DataFrame):
                return Data[0]
            elif isinstance(Data[0],list):
                ret=pd.Series(data=Data[0],index=list(range(1,len(Data[0])+1)))
                ret.name=""
                ret.index.name=""
                return ret

            else:
                raise Exception("Error, can only accept Series or Dataframe objects")

        elif len(Data)==2 :
            x=None
            y=None
            name=""
            index_name=""
            if isinstance(Data[0],pd.Series):
                x=Data[0].values
                index_name=Data[0].name
                
            if isinstance(Data[1],pd.Series):
                y=Data[1].values
                name=Data[1].name
                
            if isinstance(Data[0],list):
                x=Data[0]
                
                
            if isinstance(Data[1],list):
                y=Data[1]
                
            
            if (isinstance(Data[0],pd.Series) or isinstance(Data[0],list)) and (isinstance(Data[1],pd.Series) or isinstance(Data[1],list)):
                ret=pd.Series(data=y,index=x)
                ret.name=name
                ret.index.name=index_name
                return ret
            else:
                raise Exception("Error, when two arguments are passed in, they must both be Series, or list objects")
        else:
            raise Exception("Error, can only accept 1 or 2 arguments")
                    


    def _get_index(self,row,col,width):   
        if width==1:
        
            return (row-1)*self.ncol+col
        else:
            return((row-1)*self.ncol+col,(row-1)*self.ncol+col+width-1)


