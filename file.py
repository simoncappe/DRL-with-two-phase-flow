import numpy as np
import matplotlib.pyplot as plt

L0 = 1.6
D0 = 0.8
h = 0.6 #0.79370052598
D1 = h*D0
L1 = h*L0
theta = np.pi/5
r = 0.2
x0 = D0/2

def rot(angle):
    return np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])


t = np.linspace(0,1,10)

def line(a,b):
    return (1-t)*a+t*b

def mirror(z):
    return np.array([-z[0],z[1]])
def orto(a):
    return np.array([-a[1],a[0]])


z0 = np.array([x0,0])

def create_modl(a,b,L,D,theta,r,nb_branche = 0):
    
    z0 = rot(-theta*nb_branche)@(a-b)
    


    zc1 = z0 +r*np.array([1,0])


    z1 = rot(theta)@(z0 - zc1) + zc1 
    
    z2 = z1 - D*np.array([np.cos(theta),np.sin(theta)])
    
    z3 = z1 + L*np.array([np.sin(theta),-np.cos(theta)])
    
    z4 = z3 -D*np.array([np.cos(theta),np.sin(theta)])
    
    zc2 = np.array([0,z2[1]-z2[0]/np.tan(np.pi/2 - theta)])
    
    last = z3 - D/2 * np.array([np.cos(theta),np.sin(theta)])
    
    #pts d'intérêts supplémentaires
    
    z13 = (z1+z3)/2
    z24 = (z2+z4)/2
    
    #vecteurs d'intêtets supp:
    
 
    
    
    
    
    Zd = [z0,z1,z2,z3,z4,zc1,last,z13,z24]
    
    return Zd, zc2

b0 = np.array([0,0])
Zd, zc2 = create_modl(z0, b0,L1, D1, theta, r)
up = z0 + L0*np.array([0,1])

Zd.append(up)
Zd.append((z0+up)/2)
Zg = []
for z in Zd:
    Zg.append(mirror(z))

Z = Zg + Zd+[zc2]


Nd,nc2 = create_modl(Zd[3],Zd[6],L1*h,D1*h, np.pi/4,r*h,nb_branche=1)
Ng = []
for n in Nd:
    Ng.append(mirror(n))

N = Nd+[nc2]+Ng

"""for i in N:
    plt.scatter(i[0]/h,i[1]/h)
    
for z in Z:
    plt.scatter(z[0],z[1])"""
    

N_transf = []
for n in N:
    N_transf.append(rot(theta)@n + Zd[6])
T = []
for n in N_transf:
    T.append(mirror(n))

All = N_transf + Z+T

for i in range(len(All)):
    if i>=len(N_transf):
        plt.scatter(All[i][0],All[i][1],label = 'point n' + str(i))
    else:
        plt.scatter(All[i][0],All[i][1],marker = 'x')


#plt.legend()
plt.axis("equal")

    
plt.show()

"""with open("coords.txt",'w') as f:
    f.write("h = 0.1;")
    f.write('\n')
    for k in range(len(All)):
        vec = All[k]
        f.write('Point('+str(k+1)+') = {'+str(vec[0])+','+str(vec[1])+',0,h};')
        f.write('\n')"""
        
a = Zd[2]


b = zc2
print(a)
print(b)

print(np.sqrt(  (a[0]-b[0])**2  +(a[1]-b[1])**2))