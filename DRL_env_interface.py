# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:31:07 2024

@author: stephane.abdulnour
"""

import numpy as np
import os 

#from base_env import base_env
from Interface_pos_detection_algo import Interface_det
#from paraview.simple import *

class Interface():
    
    
    ### Create object
    def __init__(self, path):
        
        self.name = 'Interface'
        self.act_size = 2
        self.obs_size = self.act_size
        self.obs      = np.zeros(self.obs_size)
        self.path     = path
        self.x_min    = np.array([ 1.0, 1.0])
        self.x_max    = np.array([ 15.0 , 15.0])
        self.x_0      = (self.x_max + self.x_min)/2
        
        self.pos = 0.3
        self.episode = 0
        
        self.PasDeTemps = 0.01
        self.TempsFin = 20
        
        self.line_replace_in_txt('PasDeTemps', '{ Target= ' + str(self.PasDeTemps) + ' }', self.path + 'interface_control/IHM.mtc')
        self.line_replace_in_txt('TempsFin', '{ Target= ' + str(self.TempsFin) + ' }', self.path + 'interface_control/IHM.mtc')
        
        # Create vtu and screenshot folders
        self.vtu_path = self.path+'vtu/'
        self.scs_path = self.path+'screenshots/'
        os.makedirs(self.vtu_path)
        os.makedirs(self.scs_path)        
        
        self.macro_path = 'C:/Users/stephane.abdulnour/AppData/Roaming/ParaView/Macros'
        
        
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
        reward       = self.function(conv_actions)

        return reward, conv_actions
    

    ### Close environment
    def close(self):
        pass
        
        
    
    ### Reward function
    def function(self, x):
        
        pos = Interface_det(self.scs_path+'Screenshot_'+str(self.episode))
        
        return -np.abs(pos - self.pos)
    
    
    def line_replace_in_txt(self, string, line, target):

        command = "sed -i '/"+string+"/c\\"+line+"' "+target
        os.system(command)
        
        
    
    ### Run cfd and analyse results
    def cfd_solve(self, x):
        
        # Write speeds in IHM
        self.line_replace_in_txt('VEX1', '{ Data= ValeurItem 1 '+str(x[0])+'*0.7071067811865476 }', self.path + 'interface_control/IO/Parametres.mtc')
        self.line_replace_in_txt('VEY1', '{ Data= ValeurItem 1 -'+str(x[0])+'*0.7071067811865476 }', self.path + 'interface_control/IO/Parametres.mtc')
        self.line_replace_in_txt('VEX2', '{ Data= ValeurItem 1 '+str(x[1])+'*0.7071067811865476 }', self.path + 'interface_control/IO/Parametres.mtc')
        self.line_replace_in_txt('VEY2', '{ Data= ValeurItem 1 '+str(x[1])+'*0.7071067811865476 }', self.path + 'interface_control/IO/Parametres.mtc')
        
        
        # Run simulation
        os.system('cd '+self.path+'interface_control/.; touch run.lock; mpirun -n 8 /softs/cemef/cimlibxx/master/bin/cimlib_CFD_driver Principale.mtc > trash.txt;')
        
        
        # Relocate final scene to vtu folder and rename
        os.system('cp '+self.path+'interface_control/Resultats/2d/bulles_00100.vtu '+self.vtu_path+'.')
        os.system('mv ./vtu/bulles_00150.vtu '+'./vtu/bulles_'+str(self.episode)+'.vtu')
        

        # Run macro on last scene to get screenshot     
        cmd1 = 'cd '+self.macro_path+' && pvpython.exe Interface_macro.py bulles_'+str(self.episode)+' Screenshot_'+str(self.episode)+'.png'   ## Try using ';' instead of '&&' if not working
        os.system(cmd1)
        
        
        # Next episode
        self.episode += 1
        
        
        
        
        
        