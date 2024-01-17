# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:14:22 2024

@author: simon.cappe
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import array,cos,sin
from timesaver import write_border,merge,write_brick



def mirror(z):
    return array([z[0],-z[1]])
def scatter(z):
    plt.scatter(z[0],z[1])
r = 0.25
D = r/2
e = 0.125
h = 2*r
l = 0.01
epsilon = l/1000
d = 1.
L = 5.
theta = np.pi/4

ex = array([1,0])
ey = array([0,1])

a = array([cos(theta),sin(theta)])
b = array([-sin(theta),cos(theta)])


O = array([0,0])#origin
P1 = O + r*ey/2 #up
P2 = P1 + D*ex#right
P3 = P2 + h*ey#up
P4 = P3 + e*ex
P5 = P2 + e*ex
P6 = P5 + l*ex
P7 = P6 + d*a/cos(theta)
P8 = P7 + L*ex

H = [P1,P2,P3,P4,P5,P6,P7,P8]
B = list(map(mirror,H))

T = H + [O] + B

for t in T:
    scatter(t)
    
plt.axis("equal")
plt.show()



with open('buble.txt','w') as f:
    f.write('h = 0.1;\n\n')
    for p in range(len(T)):
        f.write('Point('+str(p+1)+') = {'+str(T[p][0])+','+str(T[p][1])+',0,h};\n')
        
##GeometrE

N= ['M' + str(k+1) for k in range(10)] + ['S','E1','E2','E3','W1','W2']
Names = ['border_'+n for n in N]


write_border( (1,0), r/2, O, name= 'E1')

write_border((0,-1),e/2,(P3+P4)/2,name = 'E2')
write_border((0,1),e/2,mirror((P3+P4)/2),name = 'E3')

write_border((0,-1),D/2,(P1+P2)/2,name = 'M1')
write_border((0,1),D/2,mirror((P1+P2)/2),name = 'M2')


write_border((1,0),h/2 -epsilon/100,(P3+P2)/2 ,name = 'M3')
write_border((1,0),h/2-epsilon/100,mirror((P3+P2)/2),name = 'M4')

write_border((0,-1),epsilon/2,P5,name = 'W1')
write_border((0,1),epsilon/2,mirror(P5),name = 'W2')


write_border((0,-1),l/2 + epsilon,(P5+P6)/2,name = 'M5')
write_border((0,1),l/2 + epsilon,mirror((P5+P6)/2),name = 'M6')

write_border(-a, epsilon/2, P6, name = 'M7')
write_border( b, epsilon/2, mirror(P6), 'M8')

write_border((0,-1), L/2, (P7+P8)/2, name= 'M9')
write_border((0,1), L/2, mirror((P7+P8)/2), name= 'M10')

write_border((-1,0), P8[1], (P8+mirror(P8))/2, name = 'S')

merge(Names)

with open('defs.txt','w') as f:
    for b in N:
        f.write('\t\t{ Modele = Definition'+b+' }\n')
        f.write('\t\t{ Modele = Geo'+b+' }\n')
        f.write('\t\t{ Modele = Distance'+b+' }\n')
        f.write('\n\n')

#Mais aussi les champs:

with open('fields.txt','w') as f:
    for b in N:
        f.write('{ Champ = AppartientEntree'+b+' } \n')

        

