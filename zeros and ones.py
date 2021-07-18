import numpy as np
shape = tuple(map(int,input().split()))
#It has to be a tuple since numpy.zeros and numpy.ones expect the first parameter to be a tuple

print(np.zeros(shape, dtype = np.int))
print(np.ones(shape, dtype = np.int))


