import math, random
random.seed(1)

def moving_window_average(x, n_neighbors):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    avg = []
    for i in range(n):
        avg += [sum(x[i:(i+width)])/width] 
    return avg
        
# x = [1, 5, 6, 9]                   
# n = 4
# width = 5                       
# x = [1, 1, 1, 5, 6, 9, 9, 9]  
# nn=1
# avg1 = [2,3,4,6] diff = 5.2
# nn = 2         
# avg2 = [ 2.8 , 22/5, 6 , 7.6 ]  diff = 4.8


# y = [ list0], [list1], [list2], .......[list9] ]
# y = [0, 1, 2, .......9]


R = 1000
x = [random.uniform(0, 1) for i in range(R)]

Y = [x] + [moving_window_average(x, n_neighbours) for n_neighbours in range(1, 10)]
print(len(Y))

print(Y[5][9])

