numbers = range(10)
squares = []
for number in numbers:
    square = numbers**2
    squares.append(square)
print(squares)

LIST COMPREHENSIONS

numbers = range(10)
square2 = []
square2 = [number**2 for number in numbers]
print(square2)

list = []
list = sum([i for i in range(10) if i%2!=0])
print(list)
