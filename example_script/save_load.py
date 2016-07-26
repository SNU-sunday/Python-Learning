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

#Save ASCII text file---------------------------------------------
np.savetxt('s_l.txt',b)

#Load ASCII text file---------------------------------------------
data=np.loadtxt('s_l.txt',skiprows=1)
c,d,e,f,g=data.T
print('\noriginal data \n',b)
print('\ntxt load from np.loadtxt data \n', data)
print('\ndata type =',data.dtype)
print('data demension =',data.shape)
print('\n',c,'\n',d,'\n',e,'\n',f,'\n',g)

#even if txt file has string, it can be loaded autometically
data2=np.genfromtxt('s_l.txt',dtype=None,names=('b1','b2','b3','b4','b5'))
print('\ntxt load from np.genformtxt\n',data2)
print('\ndata type =',data2.dtype)
print('data demension =',data2.shape)
print('\n',data2['b1'],'\n', data2['b2'],'\n',
      data2['b3'],'\n', data2['b4'],'\n', data2['b5'])

#Load idl save file----------------------------------------------
idldata=sp.io.readsav('idlsave.sav')
print('\nidl save file load by using sp.io.readsav')
print('You can check the loaded variable using idldata.keys()')
print('\nprint(idldata.keys())')
print(idldata.keys())

print('\nvel =',idldata['vel'])
print('astrok =',idldata['astrok'])
print('kui =',idldata['kui'])

#Save Python binary file -------------------------------------
np.savez('s_l.npz',arr1d=a,arr2d=b)
dataz=np.load('s_l.npz')
keyz=dataz.keys()

print('\nload .npz binary file by using np.load')
print('You can check the loaded variable using dataz.keys()')
print('\nprint(dataz.keys())')
print(keyz)

print('\narr1d =',dataz[keyz[0]])
print('arr2d =',dataz['arr2d'])







