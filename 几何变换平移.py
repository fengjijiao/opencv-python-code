#!/usr/bin/env python
# -*- coding:utf-8 -*-
#几何变换平移
import cv2,numpy
img = cv2.imread('3.jpg',0)
rows,cols=img.shape
matrix = numpy.empty([2,3], dtype = numpy.float32)#创建2*3的变换矩阵
matrix[0]=[1,0,20]#20表示向右平移20
matrix[1]=[0,1,60]#60表示向下平移60
#第三个参数是输出图像的尺寸中心
dst=cv2.warpAffine(img,matrix,(2*cols,2*rows))
cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()