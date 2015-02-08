import wx
import numpy as np
import math
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure
class LineShapeFrame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,style= wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size = (480,640))
        self.fig = Figure((6,6),dpi=80)
        panel = wx.Panel(self,-1)
        sizer = wx.BoxSizer(wx.VERTICAL)
        agg = FigureCanvasWxAgg(panel,-1,self.fig)
        self.point_x = []
        self.point_y = []
        sizer.Add(agg,0,wx.TOP)
        self.labelText = wx.StaticText(panel,-1,"You have not clicked! ")
        sizer.Add(self.labelText,0,wx.Top)
        panel.SetSizer(sizer)
        agg.Bind(wx.EVT_LEFT_DOWN,self.onLeftClick)
        self.clickcount = 0
        self.draw_figure()
    def onLeftClick(self,event):
        x,y = event.GetPosition()
        x,y = self.ax.transData.inverted().transform([x,y])
        self.point_x.append(x)
        self.point_y.append(-y)
        
        print "you click (%d,%d)" % (x,y)
        self.labelText.LabelText = "you click (%f,%f)" % (x,y)        
        self.clickcount = self.clickcount + 1
        self.draw_figure()
        
        
    
    def draw_figure(self):
        print("hello")
        self.fig.clf()
        x = np.linspace(0,1,480)
        y = np.sin(x * 2 * 3.14 * (8 + self.clickcount)) * x * (x + 0.5)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x,y)
        xarray = np.array(self.point_x)
        yarray = np.array(self.point_y)
        self.ax.plot(xarray,yarray,'go')
        self.fig.canvas.draw()
    

app = wx.App()
top = LineShapeFrame(None,-1,'LineFrame')
top.Show()
app.MainLoop()
