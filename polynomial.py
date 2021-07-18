import numpy as np

p = np.array(input().split(),float)
x =  int(input())

for i in range(len(p)-1,-1,-1):
    pos = len(p) -1 -i
    if pos ==x :
        print(p[i])

