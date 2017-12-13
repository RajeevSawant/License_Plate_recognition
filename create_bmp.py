
import os
from scipy.misc import imread
from scipy.misc import imsave

files = os.listdir('C:/license_plate_detection/input/positive')
#positive_data = open('./*jpg', 'w')
dirname = 'positive_bmp'
for file in files:
    filename = file.split('.')
    newname = '/home/nvidia/license_plate_detection/input/positive_bmp/' + filename[0] + '.bmp'
    im = imread('/home/nvidia/license_plate_detection/input/positive/' + file);
    imsave(newname , im)  
