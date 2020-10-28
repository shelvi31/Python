L1 = [ 1,3,4]
L2 = L1
L1[0] = 24
print(L2)    #Dynamic updation

L = [1,2,3]
M = [1,2,3]

print(L is M)
print(L==M)
print(id(M))
print(id(L))   #mutable objects can be identical in content, yet be different objects.

x=3
y=x
y=y-1
print(x)

L1 = [2,3,4]
L2 = L1
L2[0] = 24
print(L1)


if False:
    print("False!")
elif True:
    print("Now True!")
else:
    print("Finally True!")









