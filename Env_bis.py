# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:37:58 2024

@author: stephane.abdulnour
"""

import numpy as np
import matplotlib.pyplot as plt
import os 



class Interface():
    
    
    ### Create object
    def __init__(self, path):
        
        self.name = 'Interface'
        self.act_size = 2
        self.obs_size = self.act_size
        self.obs      = np.zeros(self.obs_size)
        self.path     = path
        self.x_min    = np.array([ 0.5, 0.5])
        self.x_max    = np.array([ 10.0 , 10.0])
        self.x_0      = (self.x_max + self.x_min)/2
        
        self.pos = -1/6          # in [-0.5, 0.5]
        self.episode = 0
        
        self.PasDeTemps = 0.01
        self.TempsFin = 0.5
        
        self.line_replace_in_txt('interface_position', '{ Target= ' + str(self.pos) + ' }', self.path + '/interface_control/IHM.mtc')
        
        self.line_replace_in_txt('PasDeTemps', '{ Target= ' + str(self.PasDeTemps) + ' }', self.path + '/interface_control/IHM.mtc')
        self.line_replace_in_txt('TempsFin', '{ Target= ' + str(self.TempsFin) + ' }', self.path + '/interface_control/IHM.mtc')
        
        
        
    def observe(self):
        
        # Always return the same observation
        return self.obs
    

    ### Convert actions
    def convert_actions(self, actions):

        # Convert actions
        conv_actions  = self.act_size*[None]
        x_p           = self.x_max - self.x_0
        x_m           = self.x_0   - self.x_min

        for i in range(self.act_size):
            if (actions[i] >= 0.0):
                conv_actions[i] = self.x_0[i] + x_p[i]*actions[i]
            if (actions[i] <  0.0):
                conv_actions[i] = self.x_0[i] + x_m[i]*actions[i]

        return conv_actions
    


    ### Take one step
    def step(self, actions, ep):

        # Take action and compute reward
        conv_actions = self.convert_actions(actions)
        reward,_       = self.function(conv_actions)

        return reward, conv_actions
    

    ### Close environment
    def close(self):
        pass
        
        
    
    ### Reward function
    def function(self, x):
        
        f = open(self.path+'/interface_control/Resultats/Rewards.txt','r')
        l = f.readlines()
        R = []
        T = []
        for line in l[1:]:
            r = float(line.split()[-1])
            t = float(line.split()[-2])
            T.append(t)
            R.append(-r/30)
       

        return R,T
    
    
    def line_replace_in_txt(self, string, line, target):

        command = "sed -i '/"+string+"/c\\"+line+"' "+target
        os.system(command)
        
        
    
    ### Run cfd and analyse results
    def cfd_solve(self, x):
        
        # Write speeds in IHM
        self.line_replace_in_txt('VE1', '{ Target= VE1 '+str(x[0])+' }', self.path + '/interface_control/IHM.mtc')
        self.line_replace_in_txt('VE2', '{ Target= VE2 '+str(x[1])+' }', self.path + '/interface_control/IHM.mtc')
       
        
        
        # Run simulation
        os.system('cd '+self.path+'/interface_control/.; touch run.lock; mpirun -n 8 /softs/cemef/cimlibxx/master/bin/cimlib_CFD_driver Principale.mtc > trash.txt;')

        
        return self.function(x)
    
    def plot_reward(self,x):
        
        R,T = self.function(x)
        
        plt.figure()
        plt.plot(T,R)
        plt.plot(T,[0]*len(T),label = 'goal')
        
        plt.xlabel('time (s) ')
        plt.ylabel('reward (au) ')
        plt.legend()
        plt.show()        