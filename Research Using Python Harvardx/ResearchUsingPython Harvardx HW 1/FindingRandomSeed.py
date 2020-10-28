#FINDING RANDOM SEED NUMBER
import math
A = math.pi/4
print(A)

import random
def rand():
    random.seed(1)
    B= random.uniform(-1,1)
    print(B)
rand()

#2c

import math
def distance(x, y):
    dist = math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])** 2)
    return dist

distance([0, 0], [1, 1])