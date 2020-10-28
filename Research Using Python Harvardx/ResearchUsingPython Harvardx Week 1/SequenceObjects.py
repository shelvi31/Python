# print(range(5))
#
# print(list(range(5)))
#
# print(list(range(0,10,2)))
#
# print("eight equals" + "8")
#
# x = "125000"
# y= x.isdigit()
# print(y)
#
# set1 = set()
# set1 = set(range(10))
# print(set1)
#
# males = set([1,3,4,2,5])
# print(males)
# females = set1 - males
# print(females)
# print(type(females))
# everyone = males|females   #union
# print(everyone)
# intersection = everyone & set([1,2,5,6,4])
# print(intersection)
#
# word="dbjdhsjdgydbszbxshgd"
#
# letters = set(word)
# print(len(letters))   #counted only unique and bot dublicate

x = set([1,2,3])
y = set([2,3,4])

union = set(x & y)
print(union)
H = set(x | y)
print(H)
result3 = set(H-union)
print(result3)

print(x.issubset(y))

#ways to construct dictionary

age = {}
age = dict()
age = {"Tim": 45, "Rahul":78, "CP" : 54}  #names are keys
print(age["CP"])
age["CP"] = age["CP"] +1
age["CP"] +=1
print(age["CP"])
print(age.keys())  #always remember to call a method with()
print(age.values())

age["tom"] = 50











