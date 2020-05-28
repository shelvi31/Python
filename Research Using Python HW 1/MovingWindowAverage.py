import random, math


def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    avg_list = []
    for i in range(n):
        avg = 0
        avg = (x[i]+x[i+1]+x[i+2])/width
        avg_list.append(avg)
    return avg_list


x = []
for k in range(1000):
    random_value = random.uniform(0, 1)
    x.append(random_value)

y = []
for j in range(10):
    n_neighbors = j
    y.append(moving_window_average(x, n_neighbors))
print(y)