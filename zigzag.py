# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:20:28 2024

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
phi = np.pi/5

ex = array([1,0])
ey = array([0,1])

a = array([cos(theta),sin(theta)])
b = array([-sin(theta),cos(theta)])

u = array([cos(phi),sin(phi)])
v = array([-sin(phi),cos(phi)])

ref = 0.66666


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

T = Left 
for t in T:
    scatter(t)
scatter(c)
plt.axis("equal")


P5 = P2 + D*u/(3*cos(phi))
P6 = B[1] + D*u/(3*cos(phi))
P7 = P5 - D*mirror_ex(u)/(3*cos(phi))
P8 = P6 - D*mirror_ex(u)/(3*cos(phi))

T.append(P5)
T.append(P6)

T.append(P7)
T.append(P8)


for t in T:
    scatter(t)
scatter(c)
plt.axis("equal")

with open('zigzag.txt','w') as f:
    f.write('h = 0.1; \n')
    for k in range(len(T)):
        vec = T[k]
        f.write('Point('+str(k+1)+') = {'+str(vec[0])+','+str(vec[1])+',0,h};\n')
        
#ecriture du geometre
from timesaver import write_border,write_brick,merge,write_circle
N = ['E1','E2','S','E1_bis','E2_bis','LS1','LS2','LS3','G1','G2','G3']
C = ['LS4','G4','C']
Names = ['border_' + s for s in N ] + ['circle_' + s for s in C ]

write_border(normal = -b, radius = l/2, center = (P3+P4)/2 , name = 'E1')
write_border(normal = mirror_ey(-b), radius = l/2, center = mirror_ey((P3+P4)/2) , name = 'E2')

write_border(normal = -b, radius = l/2, center = (P3+P4)/2 - (d-epsilon(d)) * b, name = 'E1_bis')
write_border(normal = mirror_ey(-b), radius = l/2, center = mirror_ey((P3+P4)/2) + (d-epsilon(d)) * a, name = 'E2_bis')

write_border(u,L*cos(phi)/2,P6- epsilon(1/10)*v/2,'LS1'  )
write_border(mirror_ex(u),L*cos(phi)/2,P6- epsilon(1/10)*v/2,'LS2'  )
write_border((0,1),1.5*d,O,'LS3')
write_circle( L*cos(phi)/2, P6, name = 'LS4')



write_border(u,L*cos(phi)*ref,P6- epsilon(1/10)*v/2,'G1'  )
write_border(mirror_ex(u),L*cos(phi)*ref,P6- epsilon(1/10)*v/2,'G2'  )
write_border((0,1),1.5*d,O,'G3')
write_circle( L*cos(phi)*ref, P6, name = 'G4')





write_circle(  epsilon(1/100), center = P5, name = 'C')
write_border((-1,0), radius = L, center = (P7+P8)/2, name='S')

merge(Names)

with open('defs.txt','w') as f:
    for n in N+C:
        f.write('{ Modele = Definition'+n + ' } \n')
        f.write('{ Modele = Geo'+n + ' } \n')
        f.write('{ Modele = Distance'+n + ' } \n')
        f.write('\n')
        
with open('appartients.txt','w') as f:
    for n in N+C:
        f.write('{ Champ = AppartientEntree'+n+' } \n' )



