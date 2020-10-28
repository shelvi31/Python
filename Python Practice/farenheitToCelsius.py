s = input() #temparature input
x = s[len(s)-1]
s1 = s.replace(x,"")

if x == "F":
    y = (float(s1) - 32)*5/9
    print(str(y)+"C")
else:
    y = (float(s1) *9/5) + 32
    print(str(y) + "F")


