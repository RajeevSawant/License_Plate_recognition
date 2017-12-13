import os

currentDirectory='C:/license_plate_detection/value_data/negative_val/'

files = os.listdir('C:/license_plate_detection/value_data/negative_val')
train_data = open('C:/license_plate_detection/value_data/train_data.txt', 'a')
for file in files:
    filename = file.split('.')
    newname = currentDirectory + file + ' ' +'0\n'

    train_data.write(newname)
