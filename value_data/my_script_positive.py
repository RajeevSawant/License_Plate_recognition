import os

currentDirectory='C:/license_plate_detection/value_data/positive_val/'

files = os.listdir('C:/license_plate_detection/value_data/positive_val')
train_data = open('C:/license_plate_detection/value_data/train_data.txt', 'w')
for file in files:
    filename = file.split('.')
    newname = currentDirectory + file + ' ' +'1\n'

    train_data.write(newname) 
