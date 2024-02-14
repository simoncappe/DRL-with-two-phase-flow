# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:39:49 2024

@author: stephane.abdulnour
"""
import subprocess as sp

macro_path = 'C:/Users/stephane.abdulnour/AppData/Roaming/ParaView/Macros'
pvp_path = 'C:/Program Files/ParaView 5.10.1-MPI-Windows-Python3.9-msvc2017-AMD64/bin/'
p1 = sp.run('pvpython.exe '+macro_path+'/toot.py', shell=True, cwd=pvp_path)

run = 1 #3
n = 4 # 640

for i in range(run):
    for k in range(n):
        p1 = sp.run('pvpython.exe '+macro_path+'/toot.py', shell=True, cwd=pvp_path)
        print(p1.returncode)