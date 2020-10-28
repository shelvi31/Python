def replace(list, X, Y):
   while X in list:
      i = list.index(X)
      list.remove(X)
      list.insert(i,Y)
   return list
   
