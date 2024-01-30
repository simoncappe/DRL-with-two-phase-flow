# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:50:40 2024

@author: simon.cappe
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, array

def scatter(z):
    label_ = 't'
    plt.scatter(z[0],z[1],label = label_)
    
def mirror_ey(z):
    return array([z[0],-z[1]])

def mirror_ex(z):
    return array([-z[0],z[1]])
def epsilon(x):
    return x/25


L = 1
l = 0.6 * L/1.6

d = 5*l
D = 10*L
theta = np.pi/4

ex = array([1,0])
ey = array([0,1])

a = array([cos(theta),sin(theta)])
b = array([-sin(theta),cos(theta)])

O = array([0,0])
PM1 = O -l*sin(theta)*ex
P1 = PM1 + (L/2-l*cos(theta))*ey #array([-l*sin(theta),L/2 -l*cos(theta)])
P2 = P1 + l * a#array([0,L/2])
P3 = P1 + d * b#array([-d*cos(theta)-l*sin(theta),d*sin(theta)+L/2 -l*cos(theta)])
P4 = P3 + l*a

H = [P1,P2,P3,P4]

B = list(map(mirror_ey,H))
c = array([((P1+P2)/2)[1]/np.tan(theta) - np.abs(P1[0]/2),0])
to_mirror = [O,P2,mirror_ey(P2)]

Left =  H + B +[O,PM1] 
Right = []
for p in to_mirror:
    Right.append(mirror_ex(p) + D * ex)




T = Left #+Right
for t in T:
    scatter(t)
scatter(c)
plt.axis("equal")

with open('interface_control.txt','w') as f:
    f.write('h = 0.1; \n')
    for k in range(len(T)):
        vec = T[k]
        f.write('Point('+str(k+1)+') = {'+str(vec[0])+','+str(vec[1])+',0,h};\n')
        
#écriture des frontières
from timesaver import write_border,write_brick,merge,write_circle

"""Borders = ['M1','M2','T1','T2','M3','M4','M5','M6','E1','E2','S1','S2']
Bricks = ['B1','B2','B3','B4'] + Borders#,'B3','B4']
Names = ['border_' + s for s in Bricks]

write_border( ex, L/2 - l*cos(theta), center = PM1, name = 'M1')
write_border( -ex, L/2 - l*cos(theta), center = Right[9], name = 'M2')

write_border( -ey , radius = D/2, center = (P2 + Right[1])/2, name = 'T1')
write_border( ey , radius = D/2, center = mirror_ey((P2 + Right[1])/2), name = 'T2')

write_border(-a,d/2 ,(P2+P4)/2,name = 'M3')
write_border(-b,d/2 ,(Right[1]+Right[3])/2,name = 'M4')
write_border(-mirror_ey(a),d/2 ,mirror_ey((P2+P4)/2),name = 'M5')
write_border(-mirror_ey(b) , d/2 ,mirror_ey((Right[1]+Right[3])/2),name = 'M6')

write_border(normal = -b, radius = l/2, center = (P3+P4)/2, name = 'E1')
write_border(normal = -a, radius = l/2, center = (Right[2]+Right[3])/2, name = 'S1')

write_border(normal = mirror_ey(-b), radius = l/2, center = mirror_ey((P3+P4)/2), name = 'E2')
write_border(normal = mirror_ey(-a), radius = l/2, center = mirror_ey((Right[2]+Right[3])/2), name = 'S2')
epsilon = l/50
write_border( -b, radius = epsilon, center = P1, name = 'B1')
write_border( -a, radius = epsilon, center = Right[0], name = 'B2')
write_border( mirror_ey(-b), radius = epsilon, center = mirror_ey(P1), name = 'B3')
write_border( mirror_ey(-a), radius = epsilon, center = mirror_ey(Right[0]), name = 'B4')"""

N = ['E1','E2','S','E1_bis','E2_bis']
Names = ['border_' + s for s in N ] + ['circle_C']

write_border(normal = -b, radius = l/2, center = (P3+P4)/2 , name = 'E1')
write_border(normal = mirror_ey(-b), radius = l/2, center = mirror_ey((P3+P4)/2) , name = 'E2')

write_border(normal = -b, radius = l/2, center = (P3+P4)/2 - (d-epsilon(d)) * b, name = 'E1_bis')
write_border(normal = mirror_ey(-b), radius = l/2, center = mirror_ey((P3+P4)/2) + (d-epsilon(d)) * a, name = 'E2_bis')

"""write_border(normal = -b, radius = l, center = (P3+P4)/2 - (d+epsilon(d)) * b, name = 'E1_ter')
write_border(normal = mirror_ey(-b), radius = l, center = mirror_ey((P3+P4)/2) + (d+epsilon(d)) * a, name = 'E2_ter')"""

write_border(normal = (-1,0), radius = np.linalg.norm(Right[0]-Right[1]), center = Right[0], name = 'S')

write_circle(epsilon(l/10),  Right[1],  'C')
"""
write_border(normal = (1,0), radius = L/2 - l*cos(theta), center = PM1, name = 'ML')

write_border(normal = (0,-1), radius = l, center = P2 + l*ex, name = 'MT')
write_border(normal = (0,1), radius = l, center = mirror_ey(P2 + l*ex), name = 'MD')"""




merge(Names)


with open('defs.txt','w') as f:
    for n in N:
        f.write('{ Modele = Definition'+n + ' } \n')
        f.write('{ Modele = Geo'+n + ' } \n')
        f.write('{ Modele = Distance'+n + ' } \n')
        f.write('\n')
        
with open('appartients.txt','w') as f:
    for n in N:
        f.write('{ Champ = AppartientEntree'+n+' } \n' )



