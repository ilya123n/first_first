#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:56:45 2018

@author: user
"""

from skimage.io import*
from numpy import*
import numpy
from skimage import*
from matplotlib import*
import matplotlib.pyplot as plt
from matplotlib.pyplot import hist



img = imread('img.png')

# построение гистограммы изображения
values, bin_edges = histogram(img.ravel(), bins=range(257))

# определение размеров изображения
y, x = img.shape

# вычисление коолличества пикселей в изображении
pix = x * y

# определение колличества пикселей в отступах(5%)
k = round(pix * 0.05)

# поиск минимального значения яркости
count = 0

for i in range(256):
    count += values[i]
    if count > k:
        x_min = i
        break

# поиск максимального значения яркости
count = 0

for i in range(255, -1, -1):
    count += values[i]
    if count > k:
        x_max = i
        break
    
print(x_min, x_max)



