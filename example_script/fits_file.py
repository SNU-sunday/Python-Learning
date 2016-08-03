# -*- coding: utf-8 -*-
"""
Fits file read

Use the astropy package to open and revise a fits file.
"""

__date__="Aug 03 2016"
__author__="Kang, J"

from astropy.io import fits
import glob
import numpy as np
import matplotlib.pyplot as plt

file=glob.glob('*.fit')
exfits=fits.open(file[0])  #simultaneously readout a fits data and its header
print(exfits[0].header['naxis'])
img=exfits[0]

# only header or image.
header=fits.getheader(file[0])
data=fits.getdata(file[0])

print(header['naxis1'])
plt.imshow(data,cmap=plt.cm.Greys_r,origin='lower')
plt.clim(0,345)
plt.colorbar()
plt.show()


