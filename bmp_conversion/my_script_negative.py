import os

currentDirectory='C:/license_plate_detection/input/negative_bmp/'

files = os.listdir('C:/license_plate_detection/input/negative_bmp')
train_data = open('C:/license_plate_detection/train_data.txt', 'a')
for file in files:
    filename = file.split('.')
    newname = currentDirectory + file + ' ' +'0\n'

    train_data.write(newname)
