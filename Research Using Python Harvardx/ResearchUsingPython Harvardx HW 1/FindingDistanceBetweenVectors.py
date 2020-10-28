# FINDING DISTANCE BETWEEN VECTORS 2e
import math, random
random.seed(1)

def rand():
    return random.uniform(-1, 1)

def distance(a, b):
    dist = math.sqrt((a[0] - b[0]) * 2 + (a[1] - b[1]) * 2)
    return dist

def in_circle(x, origin=(0, 0)):
    return distance(x, origin) < 1

R = 10000
x = [(rand(), rand()) for i in range(R)]
inside = [in_circle(x[i]) for i in range(R)]
print(sum(inside) / R)