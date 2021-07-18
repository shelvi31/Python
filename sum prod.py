import numpy as np
n,m = map(int,input().split())

a = np.zeros((n,m),int)

for i in range(n):
    a[i] = np.array(input().split(),int)

sum = np.sum(a,axis=0)

prod = np.prod(sum,axis=0)

print(prod)
