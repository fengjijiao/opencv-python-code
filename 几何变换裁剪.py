#!/usr/bin/env python
# -*- coding:utf-8 -*-
#几何变换裁剪
import cv2
img = cv2.imread('3.jpg',0)
print(img.shape)

crop_img = img[200:300, 200:360]

cv2.imshow('img', crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()