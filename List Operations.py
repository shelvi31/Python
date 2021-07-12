#Inputs of Number of inputs user want to enter:
n = int(input())

# defining empy list:
L= []

# Taking multiple inputs based on n:
for i in range(n):
    t = input().split()   # Result would be a list
#Defining List Operation with each new input
    if t[0] == "append":
        L.append(int(t[1]))
    elif t[0] == "insert":
        L.insert(int(t[1]),int(t[2]))     #insert i e: Insert integer e  at position i .
    elif t[0] == "remove":
        L.remove(int(t[1]))
    elif t[0] == "pop":
        L.pop()
    elif t[0] == "sort":
        L.sort()
    elif t[0] == "reverse":
        L.reverse()
    elif t[0] == "print":
        print(L)

