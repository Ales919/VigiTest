# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 18:10:57 2016

@author: A.Osana
"""

import cv2
import numpy as np


#=================================================
#Use for Testing only. Prefer openCV's default imshow
def imshow(image,figName = 'Figura', seconds = 0):
    cv2.imshow(figName,image)
    cv2.waitKey(seconds*1000) & 0xff #
    cv2.destroyWindow(figName)
#=================================================
    
image_size =np.array((500,500,3))  # Image size in pixels    

I_black = np.zeros(image_size)
I_reddot = np.copy(I_black)

center_of_image=(image_size[0]/2,image_size[1]/2)

#Draw red Circle
radius = 20
color = (0,0,255) #Color Order is BGR in Open cv
cv2.circle(I_reddot,center_of_image,radius,color,-1)

seconds = 4
cv2.imshow("Window", I_black)
cv2.waitKey(seconds*1000) & 0xff
cv2.imshow("Window", I_reddot)
cv2.waitKey(0) & 0xff
cv2.destroyWindow("Window")
cv2.waitKey(1) & 0xff

