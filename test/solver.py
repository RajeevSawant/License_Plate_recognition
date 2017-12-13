import caffe

solver = caffe.SGDSolver('deploy.prototxt')

niter = 400
test_interval = 10

for it in range(niter):
    solver.step(1)

    if (it % test_interval == 0):
       print "Iteration ", it, "testing ..."
       correct = 0;
       solver.test_nets[0].forward() 
       print "Training loss: ", solver.net.blobs['loss'].data
       #print "Training accuracy: ", solver.net.blobs['accuracy'].data

solver.net.save('licensePlate.caffemodel')
