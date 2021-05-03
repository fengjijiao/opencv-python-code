#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread('5.jpg')

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)