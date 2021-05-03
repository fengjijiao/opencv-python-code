#!/usr/bin/env python
# -*- coding:utf-8 -*-
#几何变换扩展缩放
#只是改变图像的尺寸大小，cv2.resize()可以实现这个功能。在缩放时推荐cv2.INTER_AREA，在拓展时推荐cv2.INTER_CUBIC（慢）和cv2.INTER_LINEAR。默认情况下所有改变图像尺寸大小的操作使用的是插值法都是cv2.INTER_LINEAR。
import cv2

img = cv2.imread('3.jpg')
#下面的None本应该是输出图像的尺寸，但是因为后面我们设置了缩放因子，所以，这里为None
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#or
#这里直接设置输出图像的尺寸，所以不用设置缩放因子
height , width =img.shape[:2]
res = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

cv2.imshow('res',res)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()