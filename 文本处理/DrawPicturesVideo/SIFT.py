import cv2
import matplotlib as mpt
import matplotlib.pyplot as plt
# import dautil as dl
from dautil import plotting
from scipy.misc import face 

""" 
# img = face()
# plt.title('Origin')
# # dl.plotting.img_show(plt.gca(), img)
# plotting.img_show(plt.gca(), img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) """


import numpy as np
import os
FILEPATH = r"C:\Users\Lizhen\Pictures\opencv"

img = cv2.imread(os.path.join(FILEPATH,'bhy-face.jpg'))
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imwrite('sift_keypoints.jpg',img)