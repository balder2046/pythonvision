import numpy as np
import matplotlib.pyplot as plt

class CDataPoints:
    currentDataIndex = 0
    epsilon = 0.001
    def __init__(self,axes,numSet=2):
        self.colors = 'rgb'
        lineinfos = list()
        for i in range(0,numSet):
            # 0 x 1 y 2 line
            lineinfo = [[],[],[]]
            lineinfo[2], = axes.plot(lineinfo[0],lineinfo[1],self.colors[i] + 'o')
            print "print line", i
            lineinfos.append(lineinfo)
        self.lineinfos = lineinfos;

    def OnMouseClick(self,event):
        if self.currentDataIndex >= len(self.lineinfos):
            return
        lineinfo = self.lineinfos[self.currentDataIndex]
        bAdd = True
        self.modifyLineInfo(lineinfo,event.xdata,event.ydata,bAdd)
        lineinfo[2].set_data(lineinfo[0],lineinfo[1])
        lineinfo[2].figure.canvas.draw()
    def OnKeyPress(self,event):
        if event.key == 'n' or event.key == 'N' :
            self.currentDataIndex = self.currentDataIndex + 1
            if self.currentDataIndex >= len(self.lineinfos):
                self.currentDataIndex = 0
        
    def modifyLineInfo(self,lineinfo,x,y,add=True):
        if add:
            lineinfo[0].append(x)
            lineinfo[1].append(y)
        else:
            count = len(lineinfo)
            for i in range(count-1,-1,-1):
                _x = lineinfo[0][i]
                _y = lineinfo[1][i]
                sq = (x - _x) * (x - _x) + (y - _y) * (y - _y)
                if (sq < self.epsilon):
                    del lineinfo[0][i]
                    del lineinfo[1][i]
    
fig = plt.figure()
axe = fig.add_subplot(111)
axe.set_xlim([0,10])
axe.set_ylim([0,10])
data = CDataPoints(axe)

axe.figure.canvas.mpl_connect("button_press_event",data.OnMouseClick)
axe.figure.canvas.mpl_connect("key_press_event",data.OnKeyPress)
plt.show()
        
        
            
        
