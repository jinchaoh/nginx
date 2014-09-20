#!/usr/bin/python
#Filename:objvar.py
class Person:
    """represents a person"""
    population = 0
    
    def __init__(self,name):
     self.name=name
     print 'initializing %s'%self.name
     Person.population +=1
    def __del__(self):
     print 'deleting%s'%self.name
     Person.population -=1
     if Person.population==0:
      print 'I am the last person'
     else:
      print 'still %d people'%Person.population
    def sayHi(self):
     print 'Hi,My name is %s'%self.name
    def howMany(self):
     print 'there are %d persion'%Person.population
H=Person('Huang')
H.sayHi()
H.howMany()
S=Person('Sunyajuan')
S.sayHi()
S.howMany()

H.sayHi()
H.howMany()
