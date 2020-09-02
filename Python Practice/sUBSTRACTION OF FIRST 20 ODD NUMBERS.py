#SUBSTRACTION OF FIRST 20 ODD NUMBERS

y = 0
for x in range(1,40,2):
    y = y-x
print(y)  

y= 0
x = 1
while x%2 != 0:
    y = y-x
    x = x+2
    if(x>39):
        break
    
print(y)