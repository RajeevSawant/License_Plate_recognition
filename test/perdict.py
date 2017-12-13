import numpy as np
import caffe
import cv2
import math
import sys

imfile = sys.argv[1]
np.set_printoptions(threshold='nan')

net = caffe.Net('deploy.prototxt','licensePlate.caffemodel', caffe.TEST)

print net.blobs['data'].data.shape

transformer = caffe.io.Transformer({"data":net.blobs['data'].data.shape})
#transformer.set_mean('data',np.full((1,), 128.0))
transformer.set_transpose('data', (2,0,1))


net.blobs['data'].reshape(1,3,90,90)

transformer.set_raw_scale('data', 255)

im =caffe.io.load_image(imfile,color=False)

print im.shape
net.blobs['data'].data[...] = transformer.preprocess('data', im)

out = net.forward()

print "Predicted:  ",out['fc8'][0]
#input_dim=tuple(net.blob['data'].shape)[1:]
img=cv2.imread(imfile)
print img.shape
if out['fc8'][0][0]>out['fc8'][0][1]:
    cv2.rectangle(img,(0,0),(img.shape[1],img.shape[1]),(255,0,0),5)
else:
    cv2.rectangle(img,(0,0),(img.shape[1],img.shape[1]),(255,0,0),5)
    cv2.putText(img, 'This one!', (230, 50), 0, 0.8, (0, 255, 0), 2)
    
cv2.imshow('uot',img)

cv2.waitKey(0)
