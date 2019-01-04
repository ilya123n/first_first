#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:37:02 2018

@author: user
"""

from skimage.io import*
from numpy import*
import numpy
from skimage import*
from matplotlib import*
import matplotlib.pyplot as plt
#from matplotlib.pyplot import hist #добавление функции построения гистограм из библиотеки matplotlib
#from numpy import histogram #добавление функции построения гистограм из библиотеки numpy

# чтение изображения из файла
img = imread('img.png')

#получение размера изображения - высоты и ширины
y, x = img.shape

#построение гистограммы с помощью функции hist из библиотеки matplotlib
#values, bin_edges, patches = hist(lol.ravel(), bins=range(257)

#аналог функции hist из библиотеки numpy без построение гистограммы
values, bin_edges = histogram(img.ravel(), bins=range(257))

 
for i in range(0, 256):
    if (values[i] > 0): # поиск ненулевого значения в гистогрмме, что бы узнать насколько необходимо сдвинуть гистограмму влево
        for j in range(0, y):
            for k in range(0, x):
                img[j, k] = img[j, k] - i # вычитание из значения каждого пикселя смещения относительно нуля
        break

#получение гистограммы нового изобращения
values_img, bin_edges_img = histogram(img.ravel(), bins=range(257))

maxim = 0

for i in range(255, -1, -1):
    if(values_img[i] > 0):
        maxim = i
        break

for i in range(0, y):
    for j in range(0, x):
        img[i, j] = (img[i, j]) *(255 / maxim)


imsave('out_img.png', img)

'''
print("MAX:", values_img.max, "MIN:", values_img.min)
print()


'''

test = imread('tiger-high-contrast.png')
imshow(test)
print(array_equal(img, test))
        

