import numpy
numpy.set_printoptions(legacy="1.13")

size = input().split()
m = int(size[0])
n = int(size[1])
print(numpy.eye(m,n))
