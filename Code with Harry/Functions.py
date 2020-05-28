#FUNCTIONS

def add(a,b):
    mysum = a+b
    return mysum

print(add(4,7))

def add_and_diff(a,b):
    mysum = a+b
    mydiff = a-b
    return (mysum,mydiff)

print ( add_and_diff(16,13))

newadd = add
print(newadd(4,5))

def modify(mylist):
    mylist[0] *= 10
    return mylist

L = [1,2,3,4,5]
print(modify(L))

def modify(mylist):
    mylist[0] *= 10
    return(mylist)
L = [1, 3, 5, 7, 9]
M = modify(L)
print(M is L)    #question


def intersect(s1,s2):
    result = []
    for x in s1:
        if x in s2:
            result.append(x)
    return (result)

print( intersect([2,3,4,5,6],[1,2,5,6,7]))

# def is_vowel(letter):
#     if letter in str("aeiouy"):
#         return(True)
#     else:
#         return(False)