d1=[]
#d1 is a list
d2={}
#d2 is a list
d3=()
#d3 is a tuple
print(type(d1))
print(type(d2))
print(type(d3))
d2={"shelvi":"pizza","sakshi":"pasta","cp":"daliya",5:7,"shubham":{"Breakfast":"pizza","L":"Roti","Dinner":"AALU"}}
print(d2)
print(d2["shelvi"])
print(d2[5])
print(d2["shubham"]["Dinner"])
d2["ankit"]=["khana"]
d2["420"]=["kababs"]
print(d2)
print(d2.copy())
del d2["cp"]
print(d2)

d3=d2
del d3["shelvi"]
print(d3)

d2.update({"leena":"toffee"})
print(d2)

print(d2.keys())
print(d2.items())
