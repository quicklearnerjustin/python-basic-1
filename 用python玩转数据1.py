# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 02:00:00 2019

@author: Jiastin
"""
#grpah
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,4,0.1)
plt.plot(t,t,t,t+2,t,t**2)

#input
sd1=int(input("the first side is"))
sd2=int(input("the second side is"))
if sd1==sd2:
    print("the square's area is", sd1*sd2)
else:
    print("the rectangle's area is", sd1*sd2)
        
#find all of the prime numbers between 2 and 100
from math import sqrt
j=2
while j<=100:
    i=2
    k=sqrt(j)
    while i<=k:
        if j%i==0:
            break
        i=i+1
    if i>k:
        print(j,end=' ')
    j+=1

#crawling
import requests
re=requests.get('http://money.cnn.com/data/dow30/')
print(re.text)

from bs4 import BeautifulSoup
markup='<p class="title"><b>The Little Prince</b></p>'
soup=BeautifulSoup(markup, "lxml")
print(soup.b)
a=soup.find_all('b')
print(a)

#tuple
def foo(args,*argst):
    print(args)
    print(argst)
a=foo("Hello","Wangdachui", "Niuyu","Linlin")
print(a)

#dictionary
ainfo={'a':3000,'b':2000,'c':5000,'d':1000}
info=[('a',3000),('b',2000),('c',5000),('d',1000)]
binfo=dict(ainfo)
cinfo=dict([['a',3000],['b',2000],['c',5000],['d',1000]])
dinfo=dict(a=3000,b=2000,c=5000,d=1000)
print(ainfo==binfo==cinfo==dinfo)
print(ainfo)
print(ainfo.keys())
print(ainfo.values())
print(ainfo.items())
for k,v in ainfo.items():
    print(k,v)
    
aDict={}.fromkeys(('a','b','c','d'),3000)
print(aDict)

names=['a','b','c','d']
salaries=[3000,2000,5000,1000]
ad=dict(zip(names,salaries))
print(ad)

pList=[('AXP','American Express',78.51),('BA','Boeing',184.76),('CAT','Caterpillar',96.39)]
aList=[]
bList=[]
cList=ainfo.update(binfo)
for i in range(len(pList)):
 aList.append(pList[i][0])
 bList.append(pList[i][2])
a=dict(zip(aList,bList))
print(a)
print(pList.get('BABA'))

#set
n=['a','b','c','c','d','a']
n1=set(n)
print(n1)

aSet=set('sunrise')
bSet=set('sunset')
aSet.add('!')
aSet.remove('u')
aSet.update('yeah')
aSet.issubset(bSet)
aSet.difference(bSet)
cSet=aSet.copy()
aSet.clear()

#numpy
import numpy as np
aArray=np.ones((3,4))
aArray=np.zeros((3,4))
print(aArray)
aArray=np.array([1,2,3])
bArray=np.array([(1,2,3),(4,5,6)])
c=np.arange(1,5,0.5)
d=np.random.random((2,2))
e=np.linspace(1,2,10,endpoint=False)

x=np.array([[1,2],[3,4]])
r1=np.linalg.det(x)
r2=np.linalg.inv(x)
r3=np.dot(x,x)

#pandas
from pandas import Series
import pandas as pd
aSer=pd.Series([1,2.0,'a'])
print(aSer)
bSer=pd.Series([1,2.0,'a'],index=[1,2,3])
print(bSer)
print(bSer.index)
print(bSer.values)
aSer=Series([3,5,7],index=['a','b','c'])
print(aSer['b'])
print(aSer*2)
print(np.exp(aSer))
data={'AXP':'86.4','CSCO':'122.64','BA':'99.44'}
sindex=['AXP','CSCO','BA','AAPL']
aSer=pd.Series(data,index=sindex)
print(aSer)
print(pd.isnull(aSer))
bSer={'AXP':'86.4','CSCO':'122.64','CVX':'23.78'}
cSer=pd.Series(bSer)
print(aSer+cSer)

data={'name':['a','b','c'],'pay':[3000,2000,1000]}
frame=pd.DataFrame(data)
print(frame)
data=np.array([('a',3000),('b',2000),('c',1000)])
frame=pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
print(frame)
print(frame.index)
print(frame.values)
print(frame.columns)
frame['name']='admin'
del frame['pay']
frame.pay.min()
print(frame[frame.pay>'1500'])