# -*- coding: utf-8 -*-
"""
File save and load

Need : numpy, scipy

Save ASCII text file
    np.savetxt('filename',arr,dtype=array_type)

Save Binary file
    1. np.save('filename.npy',struct)
    2. np.savez('filename.npz',arrname=arr,arrname2=arr2)

Load ASCII text file
    data=np.loadtxt('filename',skiprows=)
    datatemp=np.genformtxt('filename',dtype=None,names=('arr1','arr2'))
    
Load Binary file
    1.IDL save file load
        struct=sp.io.readsav('idl.sav')
    2.python binary file
        struct=np.load('filename.npy' or npz file)
    

Created on Tue Jul 26 09:28:29 2016

@author: Kang, J
"""

__author__="Kang, J"

import numpy as np
import scipy as sp

a=np.arange(101)
b=np.arange(25)
b=b.reshape((5,5))

np.savetxt('s_l.txt',b)

data=np.loadtxt('s_l.txt',skiprows=1)
print(data)
type(data)

#even if txt file has string, it can be loaded autometically
data2=np.genformtxt('s_l.txt',dtype=None,names=('b1','b2','b3','b4','b5'))
type(data2)
print(data2)
print(b1, b2, b3, b4, b5)


