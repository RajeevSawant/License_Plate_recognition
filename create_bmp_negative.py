import os
from scipy.misc import imread
from scipy.misc import imsave

files = os.listdir('/home/nvidia/license_plate_detection/input/negative')
#positive_data = open('./*jpg', 'w')
dirname = 'negative_bmp'
for file in files:
    filename = file.split('.')
    newname = '/home/nvidia/license_plate_detection/input/negative_bmp/' + filename[0] + '.bmp'
    im = imread('/home/nvidia/license_plate_detection/input/negative/' + file);
    imsave(newname , im)
