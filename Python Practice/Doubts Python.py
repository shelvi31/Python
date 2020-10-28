list1 = [9, 1, 1]
list3 = list(list1)   #copy
list2 = list1     #same
list4 = list3[:]   #copy
list1[0] = 4   
list5 = list1   #same
print(list1 is list2, list2 is list3, list3 is list4, list4 is list5)
print(list1 == list2, list2 == list3, list3 == list4, list4 == list5)

#t, f , f , f 
#t , f , t , f