#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import numpy
img = cv2.imread('3.jpg')
img2 = cv2.imread('2.jpg')
print(img.item(10,10,2))
img.itemset((10,10,2),100)   #改变像素值
print(img.item(10,10,2))
print(img.shape)   #获取图像属性(行数，列数，通道数)
print(img.size)   #获取图像的像素数
print(img.dtype)   #返回图像数据类型

#图像的ROI start(区域Copy)
ball=img2[20:50,30:80]
img[40:70,50:100]=ball
#图像的ROI end

#RGB通道拆分与合并
r,g,b=cv2.split(img)#拆分(耗时)
img=cv2.merge((r,g,b))#合并(耗时)
#或者(numpy操作，更快)
#b=img[:,:,0]#拆分b通道
#红通道全置0（numpy操作，更快）
#img[:,:,2]=0

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()