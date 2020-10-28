def check(S):
      if len(S) == 19:
         S1 = "".join(S.split())
         if S1.isdigit():
            for i in range(4,len(S),5):
               if (S[i] != " "):
                  return False
            list = [int(x) for x in S1]
            if sum(list)%10 ==0:
               return True
            else:
               return False                     
         else:
            return False    
      else:
        return False

print(check("1876 0954 325009182"))
print(check(" 5555 5555 5555 5555"))
print(check("2768 3424 2345 2358"))
print(check("0123 4567 89AB EFGH"))