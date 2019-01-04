#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:09:41 2018

@author: user
"""

from skimage.io import*
from numpy import roll
from skimage import*

def align(img, g_coord):
        
    row_g, col_g = g_coord
    
    x = img.shape[1] # высота изображения
    y = img.shape[0] # ширина изображения
    
    
    delta_g = row_g - (int)(y / 3)
    
    # обрезка по x
    x_frame = (int)(x * 0.07)
    
    # обрезка по y
    y_frame = (int)((y / 3) * 0.07)
    
    # синий канал
    img_f_b = img[y_frame : (int)(y / 3) - y_frame, x_frame : x - x_frame]
    
    # зелёный канал
    img_f_g = img[(int)(y / 3) + y_frame : 2 * (int)(y / 3) - y_frame, x_frame : x - x_frame]
    
    # красный канал
    img_f_r = img[2 * (int)(y / 3) + y_frame : 3 * (int)(y / 3) - y_frame, x_frame : x - x_frame]
    
    corr_b_g = 0
    # поиск смещения синего канала с наибольшей кореляцией с зелёным каналом
    for i in range(-15,16): 
        b_i = roll(img_f_b, i, axis = 0) # по y
        for j in range(-15, 16):
            b_ij = roll(b_i, j, axis = 1) # по x
            if (b_ij * img_f_g).sum() > corr_b_g:
                corr_b_g = (b_ij * img_f_g).sum()
                i_b = i
                j_b = j
                
    corr_r_g = 0            
                
    for i in range(-15,16):
        r_i = roll(img_f_r, i, axis = 0)
        for j in range(-15, 16):
            r_ij = roll(r_i, j, axis = 1)
            if (r_ij * img_f_g).sum() > corr_r_g:
                corr_r_g = (r_ij * img_f_g).sum()
                i_r = i
                j_r = j
                
    
    row_b = delta_g - i_b
    col_b = row_g - j_b
    
    row_r = 2 * (int)(y / 3) + delta_g - i_r
    col_r = row_g - j_r
                
    return(row_b, col_b), (row_r, col_r)