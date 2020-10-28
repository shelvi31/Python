import random
#What I would like to be able to do is roll a die not just once, but 100 times and draw histogram
import matplotlib.pyplot as plt
import numpy as np
rolls = []
for k in range(100):
    rolls.append(random.choice([1,2,3,4,5,6]))
print(rolls)
plt.hist(rolls, bins= np.linspace(0.5,6.5,7))
#plt.show()

ys= []
for rep in range(10000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y+x
    ys.append(y)
plt.hist(ys);
plt.show()


print(np.random.random())

#creating 1d array : inputing size
print(np.random.random(5))

X = np.random.random((2,5))
print(X)

#NORMAL DISTRIBUTION
Y = np.random.uniform(5,2)
print(Y)
# we can specify the length of the 1d array
Y1 = np.random.uniform(5,2,5)
print(Y1)

Y2= np.random.uniform(0,1,(2,5))
print(Y2)

import numpy as np
import matplotlib.pyplot as plt
#Choosing a random int

a = np.random.randint(1,7) # for a dice
print(a)

b = np.random.randint(1,7,(10,3))
print(b)

#The next step would be to sum over all rows of x

print(np.sum(b))

sum = np.sum(b,axis=0)
print(sum)
print(len(sum))

sum2 = np.sum(b,axis=1)   #summing over all the coloumns
print(sum2)
print(len(sum2))


C= np.random.normal(1,7,(100,10))
D= np.sum(C,axis =1)
plt.hist(D)
plt.show()

C= np.random.normal(1,7,(1000000,10))
D= np.sum(C,axis =1)
plt.hist(D)
plt.show()       #And the histogram looks even more smooth in this case


#TIME MEASUREMENT

import numpy as np
import time
import random

start_time = time.clock()
print(start_time)
ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y+x
        ys.append(y)
end_time = time.clock()
print(end_time-start_time)

start_time = time.clock()
X = np.random.randint(1,7,(1000000,10))
Y = np.sum(X,axis=1)
end_time = time.clock()
print(end_time-start_time)   #This code will run faster as its using numpy

#2.4.5: Random Walks

#Random walks

import numpy as np
import matplotlib.pyplot as plt
import random

delta_x = np.random.normal(0,1,(2,5))   #0 is mean , 1 is deviation and delta_x is displacement of the person
plt.plot(delta_x[0],delta_x[1],"go")
plt.show()

#CUMULATIVE SUMMING
X = np.cumsum(delta_x, axis=1)
plt.plot(delta_x[0],delta_x[1],"bo-")
plt.show()

#Starting the same with (0,0) position
X_0 = np.array([[0],[0]])

#Concatenation function

Final = np.concatenate((X_0,X),axis=1)
print(Final)   #notice it now starts with 0
plt.plot(Final[0],Final[1],"ro-")
plt.show()
plt.savefig("random_walks.pdf")

#Running the same code more number of times:
Y_0 = np.array([[0],[0]])
delta_y = np.random.normal(0,1,(2,100))
Y = np.cumsum(delta_y, axis=1)
Final2 = np.concatenate((Y_0,Y),axis=1)
print(Final2)   #notice it now starts with 0
plt.plot(Final2[0],Final2[1],"bo-")
plt.show()

Y_0 = np.array([[0],[0]])
delta_y = np.random.normal(0,1,(2,10000))
Y = np.cumsum(delta_y, axis=1)
Final2 = np.concatenate((Y_0,Y),axis=1)
print(Final2)   #notice it now starts with 0
plt.plot(Final2[0],Final2[1],"go-")
plt.show()