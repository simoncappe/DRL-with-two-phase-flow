# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:49:02 2024

@author: stephane.abdulnour
"""

from Env_bis import Interface

interface = Interface('C:/Users/stephane.abdulnour/Projet_Fluide/Exercices/Interface_DRL')

v = [(5,5),(6,3),(9,2)]

x = v[-1]

interface.plot_reward(x)