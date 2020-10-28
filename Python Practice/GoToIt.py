def findLine(prog, target):
    s1 = prog[0].split(" ")
    s2 = prog[1].split(" ")
    s = (s1 + s2)
    t = int(target)
    for i in range(0,len(prog)-1):
        if s[i]== t:
            return i

print(findLine(['10 GOTO 20', '20 END'], '20'))