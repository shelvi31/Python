var1=6
var2=87
print("enter var3")
var3= int(input())

#if var3>var2:
 #   print("var3 greater")
#if var3==var2:
 #   print("equal")
#else:
 #   print("lesser")

if var3>var2:
    print("var3 greater")
elif var3 == var2:  #will check only if 1st condition is false and not in every case
    print("equal")
else:
    print("lesser")

list1=[3,5,2,1]
print(5 in list1)
print(15 in list1)
if 5 in list1:
    print("yes")
else:
    print("no")

print("enter your age")
age= int(input())

if age>18 and age<101:
    print("you are eligible for driving")
elif age>7 and age<18:
    print("please visit physically to check")
elif age==18:
    print("not eligible")
else:
    print("invalid age")