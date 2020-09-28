s = input()
for char in s:
    if char =="+":
        pos = s.index("+")
        print(pos)

        n1 = ""
        for i in range(0,pos):
            n1 = n1 + s[i]
        print(n1)
        n2 = ""
        for j in range(pos+1,len(s)):
            n2 = n2 + s[j]
        print(n2)

print(int(n1)+int(n2))

