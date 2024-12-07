'''
author: levio
contact: levio123@163.com
'''
import numpy as np
from PIL import Image
ALPHA = 1.8
BETA = 60
 
def light_adjust(img, a, b):
	c, r = img.size
	arr = np.array(img)
	for i in range(r):
		for j in range(c):
			for k in range(3):
				temp = arr[i][j][k]*a+b
				if temp>255:
					arr[i][j][k] = 2*255 - temp
				else:
					arr[i][j][k] = temp
	return arr
 
def merge(im1, im2):
	a1 = np.array(im1)
	a2 = np.array(im2)
	arr = np.hstack((a1, a2))
	return arr
 
def _main():
	img = Image.open("t2.jpg")
	arr = light_adjust(img, ALPHA, BETA)
	img1 = Image.fromarray(arr)
	me = merge(img, img1)
	imgg = Image.fromarray(me)
	imgg.show()
 
_main()