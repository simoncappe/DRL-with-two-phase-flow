# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:32:53 2024

@author: stephane.abdulnour
"""

import matplotlib.pyplot as plt

filename = "Screenshot_1.png"

img = plt.imread(filename)

plt.imshow(img[240:510])
plt.show()

print(img.shape)
