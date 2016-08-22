"""
Test fisspy raster
"""


__author__="J. Kang : jhkang@astro.snu.ac.kr"
__date__="Aug 22 2016"

import fisspy
import matplotlib.pyplot as plt
import numpy as np
import glob

file=glob.glob("*_c.fts")
wv=np.array([-5,-0.5,0,0.5])
raster=fisspy.read.raster(file[0],wv,0.05)
plt.figure(figsize=(16,9))

for i in range(4):
    if i==0 :
        plt.subplot(141+i)
    else:
        plt.subplot(141+i).set_yticklabels(())
    plt.tick_params(length=10,width=2)
    plt.imshow(raster[:,:,i],cmap=fisspy.cm.ha,origin='lower')
    plt.subplots_adjust(wspace=0.01)
    plt.title(r'$\lambda$ ='+str(wv[i])+'$\AA$')
    if i !=0 : 
        plt.yticks(label=None)

plt.show()
plt.draw()
