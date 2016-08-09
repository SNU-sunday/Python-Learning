"""
Created on Tue Aug  9 09:18:52 2016

@author: User
"""

import numpy as np
import glob
import fisspy
import fisspy.doppler
import matplotlib.pyplot as plt

file=glob.glob('*_c.fts')

data=fisspy.read.frame(file[0],0,130)
mdata=data.mean((0,1))

wv=fisspy.doppler.wavecalib('6562',mdata)

s=np.abs(wv) <= 1.

wc, inten=fisspy.doppler.lambdameter(wv[s],data[:,:,s],0.2)

vel=wc/6563.*3e5

plt.imshow(vel,origin='lower')
plt.clim(-1,1)
plt.colorbar()
plt.show()