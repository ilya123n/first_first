#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:10:28 2018

@author: user
"""

from skimage.io import*
from numpy import*
from skimage import*

from my_module import align

g_coord = [508, 237]
img_f = img_as_float(imread("img.png"))

align(img_f, g_coord)