#!/usr/bin/env python
# -*- coding:utf-8 -*-
# img3=img1*ka+img2*kb
# 图片长宽必须一致
import cv2

# read two images
src1 = cv2.imread('2.jpg', cv2.IMREAD_COLOR)
src2 = cv2.imread('3.jpg', cv2.IMREAD_COLOR)

# add or blend the images
dst = cv2.addWeighted(src1, 1, src2, 1, 0.0)

# save the output image
cv2.imwrite('4.jpg', dst)