#------------Using list comprehension to iterate through loop
l1 = [char for char in "shelvi_garg"]
print(l1)

#----------------Time comparisons For Loop Vs List Comprehensions

import time

#Defining for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

# define function to implement list comprehension
def list_com(n):
    return[i**2 for i in range(n)]

 #Driver Code

# Calculate time takens by for_loop()
begin = time.time()
for_loop(10**5)    #Passing n
end = time.time()
# Display time taken by for_loop()
print("Time taken for_loop:",round(end-begin,2))

# Calculate time takens by list_comprehension()
begin = time.time()
list_com(10**5)
end = time.time()
# Display time taken by for_loop()
print('Time taken for list_comprehension:',round(end-begin,2))



#-------------------------- Nested List Comprehensions

#Using For Loop
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(2,7):
        matrix[i].append(j)
print(matrix)

#Using List Comprehensions
matrix = [[j for j in range(2,7)] for i in range(3)]
print(matrix)


#---------------------------------List Comrehensions and Lambda

#using for loop to print a table of 10
numbers = []
for i in range(1,6):
    numbers.append(i*10)
print(numbers)


#Using Lc to print a table of 10
numbers = [(i*10) for i in range(1,6)]
print(numbers)

#----USing Lambda + LC : 

# Getting square of even numbers from 1 to 10
squares = [n**2 for n in range(0,11) if n%2 ==0]
print(squares)


#Transposing a matrix using FOR Loop
x = [[10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]]

import numpy as np
trans = np.zeros([3,3])

#taking length of row
for i in range(len(x)):

#Taking length of column:
    for j in range(len(x[0])):
        trans[j][i] = x[i][j]

print(trans)

# Transposing a matrix using List Comprehension
x = [[10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]]

import numpy as np
trans1 = np.zeros([3,3])
trans1 = [[ x[i][j] for i in range(len(x)) ] for j in range(len(x[0]))]
print(trans1) 

# Another way:
trans1 = [ [i[j] for i in x] for j in range(len(x)) ]
print(trans1)

trans1 = [i for i in x]
print(trans1)



#-------------------- Change case of each character in string

string = "shelvi garg"

#using LC and lambda
list = list(map(lambda i:chr(ord(i)^32),string))
print(list)

#using LC
list = [chr(ord(i)^32) for i in string]
print(list)



#----------------------------- Reverse each string in a tuple.
string = ("geeks","for","geeks")

#-1 means the last char

list = [i[::-1] for i in string]    #give break of 1 from last element
print(list)

list = [i[::-2] for i in string]    #give break of 2 from last element
print(list)

list = [i[-1::] for i in string]      #start from last element
print(list)

list = [i[:-1:] for i in string]   #skip last element
print(list)



# ------------------Display the sum of digits of all the odd elements in a list

def sum(n):
    tsum = 0
    for ele in str(n):
        tsum = tsum + int(ele)
    return tsum
    

List = [367, 111, 562, 945, 6726, 873]

newList = [sum(i) for i in List if i%2 !=0]
print(newList)

