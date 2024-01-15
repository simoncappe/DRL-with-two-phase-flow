# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:26:32 2024

@author: simon.cappe
"""
import numpy as np
import matplotlib.pyplot as plt
from file import rot



def scatter(x,label_ = 'a'):
    plt.scatter(x[0],x[1],label = label_)

c1 =  np.array([-1.6468397552181777,-1.206645849176339])
c2 =  np.array([-0.7121621679199754,-1.8857288663219263])
c3 =  np.array([0.7121621679199754,-1.8857288663219263])


e = np.array([0,1.6])


a = np.array([0.4,1.6])
b = e
vec = a-b

normal_vec = np.array([vec[1],-vec[0]])

point = b + normal_vec

"""print(np.linalg.norm(vec)*2)
print(normal_vec)


scatter(a, label_= 'a')
scatter(b, label_= 'b')
scatter(point, label_= 'normal')


plt.axis("equal")
plt.legend()
plt.show()"""


g = -9.8*np.array([0,1])
print(rot(np.pi/4)@g,'haha')



    