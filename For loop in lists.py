x,y,z,n = map(int,input().split())
L = []
ll = []

for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range (0,z+1):
            L.append([i,j,k])


for l in range(0,len(L)):
    if ((L[l][0] + L[l][1] + L[l][2]) != n):
        ll.append(L[l])

print(L)
print(ll)


    