#upper case to lower case
 
#COnvert a character
def lowerChar(char):
   if char>="A" and char<="Z":
      return(chr(ord(char) + 32))
   else:
      return char


def lowerString(string):
    result = ""
    for i in range(0,len(string)):
       result = result + lowerChar(string[i])
    return(result)

print(lowerChar("S"))
x = lowerString("HI I AM SHELVI")
print(x)
