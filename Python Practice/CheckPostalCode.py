def postalValidate(S):
    S1 = "".join(S.split())
    print(S1)
   
    if len(S1) == 6:
        for i in range(0,len(S1),2):
           y = S1[i].isalpha()
        for j in range(1,len(S1),2):
            x = S1[j].isdigit()
        
        if (x == True and y == True):
            return(S1.upper())
        else:
            return False
    else:
        return False


print(postalValidate("g5h4f 6"))