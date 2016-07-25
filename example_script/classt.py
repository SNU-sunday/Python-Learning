# -*- coding: utf-8 -*-
"""

Class testing

Created on Tue Jul 19 19:08:42 2016

----------------------------
example)

    a=classt.class_test('name')
    a.age(age)
    a.major(major)
    a.pall()

"""
__author__= "Kang, J : jhkang@astro.snu.ac.kr"

class class_test(object):
    def __init__(self, name):
        self.name = name
    def age(self, age):
        self.age = age
    def major(self, major):
        self.major = major
    def pall(self):
        print(self.age, self.major)