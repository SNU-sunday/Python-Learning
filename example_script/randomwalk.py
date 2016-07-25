# -*- coding: utf-8 -*-
"""
Random walk test

Using the random number generator and cumulative sum.

Created on Thu Jul 21 19:02:02 2016

@author: Kang, J
"""
import matplotlib.pyplot as plt
import numpy as np


t_max=100
walkers=10000
t=np.arange(t_max)

steps=2*np.random.random_integers(0,1,(walkers,t_max))-1
position=steps.cumsum(axis=1)
distance=np.mean(position**2,axis=0)

fig=plt.figure(1,(16,11))
plt.tick_params(width=2.5,length=10)
plt.xticks(fontweight='bold',fontsize=20)
plt.yticks(fontsize=20,fontweight='bold')
plt.plot(t,np.sqrt(distance),color='black',linewidth=3)
plt.plot(t,np.sqrt(t),color='red')
plt.title('Random Walk',fontsize=20,fontweight='bold')
plt.xlabel(r'$t$',fontsize=20,fontweight='bold')
plt.ylabel('Distance',fontsize=20,fontweight='bold')
plt.legend(('real','theory'),loc=2,handlelength=3,fontsize=20)
plt.show()
