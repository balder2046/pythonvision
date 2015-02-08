import numpy as np
import matplotlib.pyplot as plt
from stattools import pca
class CDataPoints:
    currentDataIndex = 0
    epsilon = 0.001
    def __init__(self,axes,numSet=2):
        self.colors = 'rgb'
        lineinfos = list()
        self.axes = axes
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

    direction = None    
    def OnKeyPress(self,event):
        if event.key == 'n' or event.key == 'N' :
            self.currentDataIndex = self.currentDataIndex + 1
            if self.currentDataIndex >= len(self.lineinfos):
                self.currentDataIndex = 0
        if event.key == 't':
            datasets = self.GetPointSet()
            V,S,mean_X = pca(datasets[0])
            if (self.direction == None):
                self.direction, = self.axes.plot([0,0],[0,0],'b')
            limit = self.axes.get_xlim()
            limit = limit[1] - limit[0]
            print "limit ",limit
            self.direction.set_xdata([mean_X[0] - limit * V[0][0],mean_X[0] + limit * V[0][0]])
            self.direction.set_ydata([mean_X[1] - limit * V[0][1], mean_X[1] + limit * V[0][1]])
            self.direction.figure.canvas.draw()
                
            
            
        
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
    def GetPointSet(self):
        retlist = []
        for lineinfo in self.lineinfos:
            
            arr = np.zeros((len(lineinfo[1]),2))
            arr[:,0] = lineinfo[2].get_xdata()
            arr[:,1] = lineinfo[2].get_ydata()
            retlist.append(arr)
        return retlist
    
fig = plt.figure()
axe = fig.add_subplot(111)
axe.set_xlim([0,10])
axe.set_ylim([0,10])
data = CDataPoints(axe,1)

axe.figure.canvas.mpl_connect("button_press_event",data.OnMouseClick)
axe.figure.canvas.mpl_connect("key_press_event",data.OnKeyPress)
plt.show()
        
            
        
