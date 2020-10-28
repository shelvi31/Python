
p = ""
while True:
    poem = input()
    if poem == "###":
        break
    p = p + " " + poem

print(p)
p1 = p.split()
print(p1)
for word in p1:
    print(p1.count(word))

