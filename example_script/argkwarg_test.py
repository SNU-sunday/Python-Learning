"""
Argument and keyword example

"""
import glob
import numpy as np
__date__="Jul 29 2016"
__author__="J. Kang : jhkang@astro.snu.ac.kr"

def test(*args,**kwargs):
#    global args
#    global kwargs
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    z=kwargs.pop('z',False)
    print("1: exist 'z=%.2f'"%z) if bool(z) else print("1: no 'z'")
    print(type(args[0]),'size=%7.2f.'%args[0].size)
#    print(key1) if bool(key1) else print("no key1 is set")
    

f=glob.glob('D:/github/SNU-sunday/Python-Learning/example_script/*.txt')
x=np.arange(101)
y=x.copy()*0.01
z=np.array(3)
test(x,y,x=1,y=2,z=3)

def test2(x,y,z=3,key1=False,key2=True):
    
    if key1:
        print('key1 yes')
    if key2:
        print('key2 no')
    print(z)
test2(x,y,z,key2=False,key1=True)