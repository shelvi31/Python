import numpy as np

zero_vector = np.zeros(5)
print(np.zeros(5))
zero_matrix = np.zeros((5,3))

print(zero_vector)
print(zero_matrix)

x = np.array([1,2,3])
y = np.array([4,5,6])
print(y>4)

X = np.array([[1,2,3],[4,5,6]])
print(X.transpose())
Y = np.array([[2,4,6],[8,10,12]])

print(x[2])
print(x[0:2])

print(x+y)

print(X[:,1])   #access to the second column of the table
print(X[:,0])    # #access to the first column of the table

print(X[0,:])    #access to first row

print([2,4] + [ 5,6])   # list comcatenate and not add

z= np.array([1,2,5])
print(z[1:2])


a = np.array([1,2])
b = np.array([3,4,5])
c = b[1:]
print(b[a] is c)

#LINSPACE FUNCTION

import numpy as np
print(np.linspace(0,100,10))

print(np.logspace(1,2,10))

print(np.logspace((np.log10(250)),(np.log10(500)),10))
X = np.array([[1,2,3],[4,5,6]])
print(X.shape)

A = np.random.random(10)
print(A)

print(np.any(A>0.9))
print(np.all(A< 0.1))

x = 20
print ( not np.any([x%i == 0 for i in range(2, x)]))