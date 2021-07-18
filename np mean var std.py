import numpy as np
# m,n = map(int,input().split())
# a = np.zeros((m,n),float)
# for i in range(n):
#     a[i] = np.array(input().split(),float)

m = 2
n = 2

a = [[1,2],[3,4]]
    
mea = np.mean(a,axis=1)
print(mea)

var = np.var(a,axis=0)
print(var)

std = np.std(var)
print(std)
