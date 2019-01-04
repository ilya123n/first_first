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


# чтение изображения с преобразованием значений пикселей в вещественные числа
img_f = (imread('img.png')).astype('float')

# определение колличества пикселей в отступах(5%)
k = round(img_f.size * 0.05)

# создание отсортированного одномерного массива
pix_sort = sort(img_f.ravel())

# определение минимального и максимального значения пикселей
pix_min, pix_max = pix_sort[k], pix_sort[-k] 

# применение линейного выравнивания яркости
img_out= ((img_f - pix_min) * (255 / (pix_max - pix_min)))

# приведение значений пикселей к целым числам
img_out = (clip(img_out, 0, 255)).astype('uint8')

# сохранение изображения
imsave('out_img.png', img_out)
