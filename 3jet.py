# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:33:31 2024

@author: simon.cappe
"""

import numpy as np
import matplotlib.pyplot as plt

from numpy import array, cos, sin

def scatter(z):
    plt.scatter(z[0],z[1])
def mirror(z):
    return array([z[0],-z[1]])

r = 0.3 #diameter of each jet
l = 3*r
h = 1. #height of end jet
L = 3*h
theta = np.pi/4

ex = array([1,0])
ey = array([0,1])

u = array([cos(theta),sin(theta)])
v = array([-sin(theta),cos(theta)])


O = array([0,0])
P1 = O + r*ey/2
P2 = P1 + l*ex
P3 = P2 + ((h-r - 2*r*cos(theta))/2)*(h-r - 2*r*cos(theta)>0)*ey
P4 = P3 + l*v
P5 = P4 + r*u
P6 = P5 - l*v
P7 = P6 + L*ex

H = [P1,P2,P3,P4,P5,P6,P7]
B = list(map(mirror,H))
T = H+B


for p in T:
    scatter(p)
plt.axis("equal")
plt.show()

with open('threejet.txt','w') as f:
    f.write('h = 0.1;\n\n')
    for p in range(len(T)):
        f.write('Point('+str(p+1)+') = {'+str(T[p][0])+','+str(T[p][1])+',0,h};\n')
    
    
from timesaver import write_border,write_circle,merge


B = ['E1','E2','E3','S']
C = []

G = B+C


Names = ['border_' + s for s in B] + ['circle_'+s for s in C] 


write_border((1,0), r/2, O, name='E1')

write_border(v, r/2, (P4+P5)/2, name='E2')
write_border(u, r/2, mirror((P4+P5)/2), name='E3')

write_border((-1,0), h/2, (P7+mirror(P7))/2, name='S')  

        
merge(Names)    
        
        

with open('defs.txt','w') as f:
    for b in G:
        f.write('\t\t{ Modele = Definition'+b+' }\n')
        f.write('\t\t{ Modele = Geo'+b+' }\n')
        f.write('\t\t{ Modele = Distance'+b+' }\n')
        f.write('\n\n')

#Mais aussi les champs:

with open('fields.txt','w') as f:
    for b in G:
        f.write('{ Champ = AppartientEntree'+b+' } \n')