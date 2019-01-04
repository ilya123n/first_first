from skimage.io import*
from numpy import*
from skimage import*
from matplotlib import*
import matplotlib.pyplot as plt



img_f = img_as_float(imread("img.png"))

x = img_f.shape[1] # высота изображения
y = img_f.shape[0] # ширина изображения
#print(y, x)

#контрольная точка на зелёном канале (y, x)

point = [508, 237] 

print(type(point))

delta_g = point[0] - (int)(y / 3)

# обрезка по x
x_frame = (int)(x * 0.07)

# обрезка по y
y_frame = (int)((y / 3) * 0.07)

# синий канал
img_f_b = img_f[y_frame : (int)(y / 3) - y_frame, x_frame : x - x_frame]
#imshow(img_f_b)
#plt.show()

# зелёный канал
img_f_g = img_f[(int)(y / 3) + y_frame : 2 * (int)(y / 3) - y_frame, x_frame : x - x_frame]
#imshow(img_f_g)
#plt.show()

# красный канал
img_f_r = img_f[2 * (int)(y / 3) + y_frame : 3 * (int)(y / 3) - y_frame, x_frame : x - x_frame]
#imshow(img_f_r)
#plt.show()

corr_b_g = 0

# поиск смещения синего канала с наибольшей кореляцией с зелёным каналом
for i in range(-15,16): 
    b_i = numpy.roll(img_f_b, i, axis = 0) # по y
    for j in range(-15, 16):
      b_ij = numpy.roll(b_i, j, axis = 1) # по x
      if (b_ij * img_f_g).sum() > corr_b_g:
            corr_b_g = (b_ij * img_f_g).sum()
            i_b = i
            j_b = j
            
b_max = numpy.roll(img_f_b, i_b, axis = 0)
b_max = numpy.roll(b_max, j_b, axis = 1)
            
     
            
corr_r_g = 0


# поиск смещения красного канала с наибольшей кореляцией с зелёным каналом            
for i in range(-15,16):
    r_i = numpy.roll(img_f_r, i, axis = 0)
    for j in range(-15, 16):
      r_ij = numpy.roll(r_i, j, axis = 1)
      if (r_ij * img_f_g).sum() > corr_r_g:
            corr_r_g = (r_ij * img_f_g).sum()
            i_r = i
            j_r = j
            
print(i_r, j_r)
            
print("delta = ", delta_g)
            
print("синий канал:", delta_g - i_b, point[1] - j_b)

print("красный канал:", 2 * (int)(y / 3) + delta_g - i_r, point[1] - j_r)
            
r_max = numpy.roll(img_f_r, i_r, axis = 0)
r_max = numpy.roll(r_max, j_r, axis = 1)


final = dstack((r_max, img_f_g, b_max))
imshow(final)


            
            
            
#img_f_b = numpy.roll(img_f_b, 15, axis = 0)            
#imshow(img_f_b)
#plt.show()
#print(corr)
'''          
for j in range(-15,15):        
    img_f_b = numpy.roll(img_f_b, j, axis = 1)
    if (img_f_b * img_f_g).sum() > corr:
            corr = (img_f_b * img_f_g).sum()
            print("j(max) = ", j)
            
print(corr)
'''