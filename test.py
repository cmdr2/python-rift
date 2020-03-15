#!/usr/bin/python

from openhmd import PyOpenHMD

foo = PyOpenHMD()

while True:
  foo.poll()
  print("rotation quat: %f %f %f %f" % (foo.rotation[0], 
    foo.rotation[1], 
    foo.rotation[2], 
    foo.rotation[3]))
  print("acc vec: %f %f %f" % (foo.acceleration[0],
    foo.acceleration[1],
    foo.acceleration[2]))
  print("gyro vec: %f %f %f" % (foo.gyro[0],
    foo.gyro[1],
    foo.gyro[2]))
  print("left projection matrix: %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f" % (foo.leftprojectionmatrix[0], 
    foo.leftprojectionmatrix[1], 
    foo.leftprojectionmatrix[2], 
    foo.leftprojectionmatrix[3], 
    foo.leftprojectionmatrix[4], 
    foo.leftprojectionmatrix[5], 
    foo.leftprojectionmatrix[6], 
    foo.leftprojectionmatrix[7], 
    foo.leftprojectionmatrix[8], 
    foo.leftprojectionmatrix[9], 
    foo.leftprojectionmatrix[10], 
    foo.leftprojectionmatrix[11], 
    foo.leftprojectionmatrix[12], 
    foo.leftprojectionmatrix[13], 
    foo.leftprojectionmatrix[14], 
    foo.leftprojectionmatrix[15]))
