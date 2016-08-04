"""
FISS READ FRAME test

If don't now how to use the fisspy.read package,
please read the docstring of that module.

"""

__author__="J. Kang : jhkang@astro.snu.ac.kr"
__date__="Aug 04 2016"

import fisspy
import matplotlib.pyplot as plt
import glob
from mpl_toolkits.axes_grid1 import make_axes_locatable as mkl

file_pca=glob.glob('*_c.fts')
file_upca=glob.glob('*A1.fts')

data_pca=fisspy.read.frame(file_pca[0],70,80)
data_upca=fisspy.read.frame(file_upca[0],70,80,pca=False)
xmax=data_pca.shape[2]
plt.figure(1)
plt.plot(data_pca[0,125,:])
plt.xlim([0,xmax])
plt.title('FISS Spectral Profile')
plt.show()

plt.figure(2,(16,9))
ax=plt.gca()
plt.plot([0,512],[125,125],linestyle='dashed',color='white')
im=plt.imshow(data_pca[0,:,:],cmap=fisspy.cm.ha,origin='lower')
plt.title('FISS Spectrogram at X=%i'%70)
#plt.axis('off')
divider=mkl(ax)
cax=divider.append_axes("right",size='3%',pad=0.055)
plt.colorbar(im,cax=cax,ticks=[1500,4000,7500])
plt.show()
