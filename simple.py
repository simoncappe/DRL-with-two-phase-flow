# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:32:45 2024

@author: simon.cappe
"""

import numpy as np
import matplotlib.pyplot as plt
from timesaver import write_border,merge,write_brick


def scatter(x,label_ = 'a'):
   
    plt.scatter(x[0],x[1],label = label_)
def mirror(z):
    return np.array([z[0],-z[1]])

L = 5.
l = 10.
r = 1.5
epsilon = r/5
ex = np.array([1,0])
ey = np.array([0,1])

p0 = np.array([0,0]) #origin

p1 = np.array([0,L/2])#end top top left
p2 = np.array([0,L/2-r])#end top bottom left

p3 = np.array([-2*r,L/2])#begin top top left
p4 = np.array([-2*r,L/2-r])#begin top bottom left

p5,p6,p7,p8,p9 = p0+l*ex,p1+l*ex,p2 + l*ex,p3 + (l+4*r)*ex,p4 + (l+4*r)*ex


P = [p1,p2,p3,p4,p6,p7,p8,p9]
P_ = list(map(mirror,P))

P_p = P+[p0,p5]  +P_


for p in range(len(P_p)):
    scatter(P_p[p],str(p+1))
   
plt.axis("equal")
plt.legend()
plt.show()


### création du mesh:
with open('laminar_control.txt','w') as f:
    f.write('h = 0.1;\n\n')
    for p in range(len(P_p)):
        f.write('Point('+str(p+1)+') = {'+str(P_p[p][0])+','+str(P_p[p][1])+',0,h};\n')
#Ecritutre de GeometrE:
write_border((1,0),r/2,(p3+p4)/2,'E1')#entrée haut
write_border((-1,0),r/2,(p8+p9)/2,'S1')#Sortie haut

write_border((1,0),r/2,(P_[2]+P_[3])/2,'E2')#Entree Bas
write_border((1,0),r/2,mirror((p8+p9)/2),'S2')#Sortie bas

write_border((1,0),L/2-r-epsilon,p0,'C1') #Mur vertical gauche
write_border((-1,0),L/2-r-epsilon,p5,'C2') #Mur Vertical droit

#Murs d'en haut et en bas décomposés:
write_border((0,-1),r,(p3+p1)/2,'H1')
write_border((0,-1),r,(p6+p8)/2,'H3')
write_border((0,-1),L/2,(p1+p6)/2,'H2')

write_border((0,1),r,(P_[2]+P_[0])/2,'B1')
write_border((0,1),r,(P_[4]+P_[6])/2,'B3')
write_border((0,1),L/2,(P_[0]+P_[4])/2,'B2')
#fin, place aux quatre briques :

write_border( (1,0), radius = epsilon, center = p2, name = 'G1')
write_border( (1,0), radius = epsilon, center = mirror(p2), name = 'G2')

write_border( (-1,0), radius = epsilon, center = p7, name = 'D1')

write_border( (-1,0), radius = epsilon, center = mirror(p7), name = 'D2')

#fini

B = ['E1','E2','S1','S2','C1','C2','H1','H2','H3','B1','B2','B3','G1','G2','D1','D2']


N = ['border_'+B[k] for k in range(12)] + ['border_'+B[k] for k in range(12,len(B))]

merge(N)
 
#On peut écrire les définitions si on veut :

with open('defs.txt','w') as f:
    for b in B:
        f.write('\t\t{ Modele = Definition'+b+' }\n')
        f.write('\t\t{ Modele = Geo'+b+' }\n')
        f.write('\t\t{ Modele = Distance'+b+' }\n')
        f.write('\n\n')

#Mais aussi les champs:

with open('fields.txt','w') as f:
    for b in B:
        f.write('{ Champ = AppartientEntree'+b+' } \n')