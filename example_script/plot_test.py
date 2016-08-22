# -*- coding: utf-8 -*-
"""
Plot example

Use some modules and those functions to make beutiful plot for own purpose

You can read the full code by typing command line "plot_test??" on the ipython
console or ctrl+left_click on the spyder text editor after importing this code.

If you want to plot a graph on new window interactively change the backend of
your console
ex) on the ipython console type "%matplotlib", where % can be omitted


Created on Wed Jul 20 14:49:42 2016

@author : Kang, J
-----------------------------------------------
Show an example of the way how to use matplotlib.

"""

__author__= "Kang,J : jhkang@astro.snu.ac.kr"

import matplotlib.pyplot as plt
import numpy as np


#Variable
x=np.linspace(0,100,11)
y=2*x.copy()

#figure size -----------------------------------------------
fig=plt.figure(1,figsize=(16,10))
#ax=fig.add_subplot(111)

#font setup-------------------------------------------------
#usually the Helvetica is the default font
#hfont=['fontname':'Helvetica']
#plt.rcParams['font.family']='Helvetica'
#plt.subplot(111)

#plot -----------------------------------------------------------
#ax=plt.subplot(111)
plt.plot(x,x,color='black',linestyle='solid',marker='o',markerfacecolor='red',
         markersize=7,markeredgecolor='blue',linewidth=2)
plt.plot(x,y,color='blue',linestyle='dashed',marker='+',
         markerfacecolor='green',markersize=10,markeredgecolor='green',
         linewidth=2,markeredgewidth=2)

#create the text on the graph
plt.annotate('SDO/AIA 171',xy=(25,25),color='blue',fontsize=20,
             fontweight='bold')             
plt.text(15,15,'plt.text',fontsize=20,fontweight='bold')

#plot symbol on the graph
plt.plot([75],[75],'o',markerfacecolor='green',markersize=10,
         markeredgecolor='black')

#arrow mark and text
plt.annotate("I'M OUTSIDER",xy=(75,75),xytext=(80,60),color='black',
             fontsize=20,arrowprops=dict(facecolor='red',shrink=0.05),
             fontweight='bold')
             
#legendary
plt.legend(('line1','line2'),loc=1,fontsize=20,handlelength=3)


#Axes & Tick setup----------------------------------------------------
plt.rc('axes',linewidth=2.5)
plt.ylim([0,100])

plt.tick_params(width=2.5,length=10,direction='out',axis='y')
plt.tick_params(width=2.5,length=10,direction='in',axis='x')

#If you wnat to set minorticks,
#ax.minorticks_on()
#ax.thick_params(width=1,length=5,which='minor')

#if you want to set tick in each axes,
plt.xticks(np.linspace(0,100,5),fontsize=20,fontweight='bold')
plt.yticks(np.linspace(0,100,6,endpoint=True),fontsize=20,fontweight='bold')

#if you want to set tick as string
#plt.xticks(np.linspace(0,100,5),['name',r'$\alpha$',r'$0$','d','f'])
#axis range

#Title--------------------------------------------------------

plt.xlabel(r'IMX-axis $\mathbf{\gamma}$',fontsize=20,fontweight='bold')
plt.ylabel(r'IMx-axis $\mathbf{\alpha}$',fontsize=20,fontweight='bold')
plt.title(r'SDO/AIA 171 $\mathbf{\AA}$',fontsize=20,fontweight='bold')


#invert axes-------------------------------------------------
#ax.inver_xaxis()

#show the image---------------------------------------------
plt.show()

#2d image--------------------------------------------------
a=np.arange(25)
b=a.reshape((5,5))-12
fig=plt.figure(2,figsize=(16,10))
plt.imshow(b,cmap=plt.cm.Greys_r,origin='lower')
plt.clim(-10,10)   # color bar limit
plt.xticks([0,2,4],fontsize=20)
plt.colorbar(ticks=[-10,0,10])
plt.show()
#You have to causion that python plot 2d array from left top to right bottom
#But IDL plot 2d array from left bottom to top right