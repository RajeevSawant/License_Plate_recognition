import os

currentDirectory='C:/license_plate_detection/input/positive_bmp/'

files = os.listdir('C:/license_plate_detection/input/positive_bmp')
train_data = open('C:/license_plate_detection/train_data.txt', 'w')
for file in files:
    filename = file.split('.')
    newname = currentDirectory + file + ' ' +'1\n'

    train_data.write(newname) 
