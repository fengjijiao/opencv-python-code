#!/usr/bin/env python
# -*- coding:utf-8 -*-
# img3=img1+img2
# 图片长宽必须一致
import cv2
import numpy
img = cv2.imread('3.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.add(img, img2)
cv2.imshow('image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()