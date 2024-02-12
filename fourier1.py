# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:42:09 2024

@author: simon.cappe
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import cos,sin
from scipy.integrate import quad


def affine(x1,y1,x2,y2,x):
    return y2*(x-x1)/(x2-x1) + y1*(x-x2)/(x1-x2)



valeur_maximale = 1.
step1 = valeur_maximale *0.95
frequence = 10
periode = 1/frequence
epsilon = periode/20
eps = valeur_maximale/20
montee = 0.75*periode
descente1 = 0.1*periode
descente2 = descente1



t = np.linspace(0,periode*1,300)


print((montee+epsilon+descente1)/periode)


def f(x):
    x_ = (x-int(x/periode)*periode)
    if x_<montee-descente2:
        return step1*x_/(montee-descente2)
    elif x_<montee:
        return affine(montee-descente2,step1,montee,valeur_maximale,x_)
    elif x_<montee+epsilon:
        return valeur_maximale
    elif x_<montee+epsilon+descente1:
        return affine(montee+epsilon+descente1,step1,montee+epsilon,valeur_maximale,x_)
    else:
        return affine(periode,0,montee+descente1+epsilon,step1,x_)
    
    
I = np.vectorize(f)(t)
#plt.axis("equal")
plt.plot(t,I)






"""
def F(x):
    return quad(f,x,x+epsilon)[0]/epsilon
J = np.vectorize(F)(t)

#plt.plot(t,J,label = 'F')

def G(x):
    return quad(F,x,x+epsilon,epsabs=0.01)[0]/epsilon
K = np.vectorize(G)(t)
#plt.plot(t,K,label = 'G')

def H(x):
    return quad(G,x,x+epsilon,epsabs=0.01)[0]/epsilon
L = np.vectorize(H)(t)
plt.plot(t,L,label = 'H')


"""




def c_n(x,n):
    return cos(n*x*2*np.pi*frequence)
def s_n(x,n):
    return sin(n*x*2*np.pi*frequence)



n = 10
offset = quad(f,0,periode)[0]/periode
A = []
B = []
for k in range(1,n+1):
    def f_a(x):
        return c_n(x,k)*f(x)
    A.append(2*quad(f_a,0,periode)[0]/periode)
    def f_b(x):
        return s_n(x,k)*f(x)
    B.append(2*quad(f_b,0,periode)[0]/periode)
    
A,B = np.array(A),np.array(B)

def approche(x):
    C = np.array([c_n(x, k) for k in range(1,n+1)])
    S = np.array([s_n(x, k) for k in range(1,n+1)])
    
    return  np.sum(A*C) + np.sum(B*S) +offset
Z = np.vectorize(approche)(t)

plt.plot(t,Z) 
plt.show()  


print(A,B)



def write_champ(name,value):
    texte = """
        { Champ=
             { Type= P1_Scalaire_Par }
             { Nom= """+name+""" }
             { Data= ValeurItem 1 """+str(value)+""" }
        }"""
    return texte


with open('fourier_coef.txt','w') as file:
    file.write(write_champ('offset', offset))
    file.write('\n')
    for k in range(n):
        file.write(write_champ('int'+str(k+1), value = k+1))
        file.write('\n')
        file.write(write_champ('a'+str(k+1), A[k]))
        file.write('\n')
        file.write(write_champ('b'+str(k+1), B[k]))
        file.write('\n')
 
        
 
with open('declarations.txt','w') as file:
    for k in range(n):
        file.write('{ Champ= a'+str(k+1)+' }\n')
        file.write('{ Champ= b'+str(k+1)+' }\n')
        file.write('{ Champ= int'+str(k+1)+' }\n')
        
        
with open('operations.txt','w') as file:
    file.write('{ Operation = F = offset } \n')
    file.write('{ Operation = C = Zero } \n')
    file.write('{ Operation = S = Zero } \n')
    for k in range(n):
        file.write('{ Operation = C_tmp = Temps } \n')
        file.write('{ Operation = C_tmp *= omega } \n')
        file.write('{ Operation = C_tmp *= int'+str(k+1)+' } \n')
        file.write('{ Operation = C_tmp Cos C_tmp } \n')
        file.write('{ Operation = C_tmp *= a'+str(k+1)+' } \n')
        file.write('{ Operation = C += C_tmp } \n')
        file.write('\n')
        file.write('{ Operation = S_tmp = Temps } \n')
        file.write('{ Operation = S_tmp *= omega } \n')
        file.write('{ Operation = S_tmp *= int'+str(k+1)+' } \n')
        file.write('{ Operation = S_tmp Sin S_tmp } \n')
        file.write('{ Operation = S_tmp *= a'+str(k+1)+' } \n')
        file.write('{ Operation = S += S_tmp } \n')
        file.write('\n //##\n')

    
        

    


