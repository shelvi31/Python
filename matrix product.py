import numpy as np
n = int(input())


a = np.zeros((n,n),int)
b = np.zeros((n,n),int)
for i in range(n):
    a[i] = np.array(input().split(" ",n),int)
for i in range(n):
    b[i] = np.array(input().split(" ",n),int)

# m = 2
# n = 2

# a = [[1,2],[3,4]]

# b = [[1,2],[3,4]]

print(np.dot(a,b))