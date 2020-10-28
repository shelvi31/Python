def choose(n,k):
   p = 1
   for i in range(n,n-k,-1):
      p = p * i
   for j in range(k,0,-1):
      p = p/j
   return p