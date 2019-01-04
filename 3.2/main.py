#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:10:52 2018

@author: user
"""

from skimage.io import*
from numpy import*
import numpy
from skimage import*
from matplotlib import*
import matplotlib.pyplot as plt

# чтение изображения с преобразованием значений пикселей в вещественные числа
img_f = img_as_float(imread('img.png'))

# перевод изображения в пространство YUV
Y = 0.2126*img_f[:, :, 0] + 0.7152*img_f[:, :, 1] + 0.0722*img_f[:, :, 2]
U = -0.0999*img_f[:, :, 0] - 0.3360*img_f[:, :, 1] + 0.4360*img_f[:, :, 2]
V = 0.6150*img_f[:, :, 0] - 0.5586*img_f[:, :, 1] - 0.0563*img_f[:, :, 2]

# определение колличества пикселей в отступах(5%)
k = round(Y.size * 0.05)

# создание отсортированного одномерного массива
pix_sort = sort(Y.ravel())

# определение минимального и максимального значения пикселей
pix_min, pix_max = pix_sort[k], pix_sort[-k]

# применение линейного выравнивания яркости для канала Y
Y = ((Y - pix_min) * (1 / (pix_max - pix_min)))

Y = clip(Y, 0, 1)

R = Y + 1.2803*V
G = Y - 0.2148*U - 0.3805*V
B = Y + 2.1279*U

imsave('out_img.png', img_as_ubyte(clip(dstack((R, G, B)), 0, 1)))
