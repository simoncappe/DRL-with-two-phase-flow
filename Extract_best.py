# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:15:23 2024

@author: stephane.abdulnour
"""

files = ['resultsFLO_17-48-270Sumup.txt', 'resultsFLO_17-48-271Sumup.txt', 'resultsFLO_17-48-272Sumup.txt']

reward_min = 100
VE1_min = 0
VE2_min = 0

for file in files:
    f = open(file)
    lines = f.readlines()
    
    
    for line in lines[1:]:
        r = line.split()
        
        if (r == [])or(r[0]=='path'):
            continue
        
        reward = -float(r[-1])
        VE1 = float(r[2][:-1])
        VE2 = float(r[4])
        
        if reward < reward_min:
            reward_min = reward
            VE1_min = VE1
            VE2_min = VE2
     
print('Simulation : FLO_A3 \n')
print('VE1_min = '+ str(VE1_min) + '\n')
print('VE2_min = '+ str(VE2_min) + '\n')
print('Reward_min = '+ str(-reward_min) + '\n')
    
    


    