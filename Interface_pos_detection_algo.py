# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:11:35 2024

@author: stephane.abdulnour
"""

import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



def Interface_det(argv):
    
    def get_minmax_values(table):
        min_values = []
        max_values = []
        for i in range(len(table)):
            min_value = min(table[i])
            min_values.append(min_value)
            max_value = max(table[i])
            max_values.append(max_value)

        return min(min_values), max(max_values)
    
    def rgb_to_gray(image):
        n,p,*_ = np.shape(image)
        new_img = np.zeros((n,p))
        for i in range(n):
            for j in range(p):
                new_img[i,j] = np.average(image[i,j])
        
        return new_img
    
    default_file = 'Horiz_flow.png'
    filename = argv[0] if len(argv) > 0 else default_file
    
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    
    #gray = rgb_to_gray(src)
    gray = cv.cvtColor(src[12:225, 40:242], cv.COLOR_BGR2GRAY)
    
    
    gmin, gmax = get_minmax_values(gray)
    
    gray = np.round((gray - gmin)*255.0/(gmax-gmin))
    
    _, BkWt = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    
    mean = np.mean(BkWt)/255
    
    print(mean)
    
    plt.imshow(BkWt, 'gray', vmin=0,vmax=255)
    plt.show()
    
    cv.waitKey(0)

    
    return mean

if __name__ == "__main__":
    Interface_det(sys.argv[1:])
    