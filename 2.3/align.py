#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:09:41 2018

@author: user
"""

from skimage.io import*
from numpy import*
from skimage import*
from matplotlib import*
import matplotlib.pyplot as plt

def align(img, g_coord):
    row_g, col_g = g_coord
    
    x = img_f.shape[1] # высота изображения
    y = img_f.shape[0] # ширина изображения
    
    
    delta_g = point[0] - (int)(y / 3)
    
    # обрезка по x
    x_frame = (int)(x * 0.07)
    
    # обрезка по y
    y_frame = (int)((y / 3) * 0.07)
    
    # синий канал
    img_f_b = img_f[y_frame : (int)(y / 3) - y_frame, x_frame : x - x_frame]
    
    # зелёный канал
    img_f_g = img_f[(int)(y / 3) + y_frame : 2 * (int)(y / 3) - y_frame, x_frame : x - x_frame]
    
    # красный канал
    img_f_r = img_f[2 * (int)(y / 3) + y_frame : 3 * (int)(y / 3) - y_frame, x_frame : x - x_frame]
    
    corr_b_g = 0
    # поиск смещения синего канала с наибольшей кореляцией с зелёным каналом
    for i in range(-15,16): 
        b_i = numpy.roll(img_f_b, i, axis = 0) # по y
        for j in range(-15, 16):
            b_ij = numpy.roll(b_i, j, axis = 1) # по x
            if (b_ij * img_f_g).sum() > corr_b_g:
                corr_b_g = (b_ij * img_f_g).sum()
                row_b = i
                col_b = j
                
    for i in range(-15,16):
        r_i = numpy.roll(img_f_r, i, axis = 0)
        for j in range(-15, 16):
            r_ij = numpy.roll(r_i, j, axis = 1)
            if (r_ij * img_f_g).sum() > corr_r_g:
                corr_r_g = (r_ij * img_f_g).sum()
                row_r = i
                col_r = j
                
                
    print("!!!!!!!!!!!!!!!!!")
                
    return(row_b, col_b), (row_r, col_r)