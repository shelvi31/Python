#USING WHILE LOOP

s = ""
string = "patience is the key!"
s = s + chr(ord(string[0])-32)
i = 1
while ( i < len(string)):
    if string[i] != " ":
        s = s + string[i]
        i = i+1
    else:
        s = s + string[i]    #push blank
        s = s + chr(ord(string[i+1])-32)
        i = i + 2
print(s)