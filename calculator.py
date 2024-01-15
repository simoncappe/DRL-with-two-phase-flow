
import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
from timesaver import write_border,merge

def scatter(x,label_ = 'a'):
    plt.scatter(x[0],x[1],label = label_)

def mirror(z):
    return np.array([z[0],-z[1]])

L = 0.5  # Diametre du grand tuyau
l = 0.5/3 # diametre du petit tuyau
theta = np.pi/4
costheta = np.cos(theta)
sintheta = np.sin(theta)

W = [(0, 0),( -l*sintheta, L/2 - l*costheta),(0, L/2 ),(5 * L,L/2),(- 5 * l,  5*l * sintheta/costheta),(- 5 * l + l *costheta,  5*l * sintheta/costheta + l *sintheta)]


H = []

for p in W:
    H.append(np.array([p[0],p[1]]))


B = []

for p in range(1,len(H)):
    B.append(mirror(H[p]))

T = H +B

for t in range(len(H)):
    scatter(H[t],label_ = str(t))

"""with open("setup_scale.txt",'w') as f:
    f.write('h = 0.001;\n')
    for k in range(len(T)):
        vec = T[k]
        f.write('Point('+str(k+1)+') = {'+str(vec[0])+','+str(vec[1])+',0,h};\n')"""
        
#calcul de points d'intérêts en plus

p1 = np.array([-l*sintheta  , 0]) #point pour la frontière verticale à l'entrée
scatter(p1,'p1')

p2 = (H[2] + H[1])/2# centre pour entrée du haut
scatter(p2,'p2')



p3 = (H[5] + H[2])/2#centre pour paroi haut gauche
scatter(p3,'p3')

p4 = (H[4]+H[1])/2
scatter(p4)

p5 = (H[2] + H[3])/2
scatter(p5)

Pp_haut = [p1,p2,p3,p4,p5]
Pp_bas = list(map(mirror, Pp_haut))

Pp = Pp_haut + Pp_bas



plt.legend()
plt.axis("equal")
plt.show()





"""write_border( ( 1 , 0 ),  L/2 - l*costheta, p1 , name = 'B1')
write_border( (cos(theta),-sin(theta)),  l/2 ,  p2, 'B2')

             
write_border((cos(theta),sin(theta)), l/2,  mirror(p2), 'B3')
             

write_border((0,-1), 5*L/2,  p5, 'B4')
write_border((0,1),  5*L/2,mirror(p5),'B5')
write_border((-1,0), L/2, (5*L,0), 'B6')


merge(['border_B' + str(i) for i in range(1,7)])"""

                          
write_border(normal = (1,0), radius = L, center = (0,0), name = 'W1')
             


             






