#SUBSTRACTION OF FIRST 20 ODD NUMBERS

# y = 0
# for x in range(1,40,2):
#     y = y-x
# print(y)  

# y= 0
# x = 1
# while x%2 != 0:
#     y = y-x
#     x = x+2
#     if(x>39):
#         break
    
# print(y)

#CONVERT a TO A

# x = input("enter your value: ")
# value1 = ord(x)
# value2 = ord(x)-32
# value3 = chr(value2)
# x = value3
# print(x)

# output single element in single line

# x = input("enter your string: ")
# for letters in x:
#     print(letters)
 
# CONVERSION to  CAPITAL

# string = input("enter your string: ")
# string_length = len(string)
# string_new = ""

# for i in range(string_length):

#     if i == 0:
#         z = string[0]
#         val1 = ord(z)
#         val2 = ord(z)-32
#         val3 = chr(val2)
#         string_new = string_new + val3
#         i = 1

#     elif:
#         if string[i] == " ":
#             y = string[i+1]
#             value1 = ord(y)
#             value2 = ord(y)-32
#             value3 = chr(value2)
#             string_new = string_new + " " + value3
#             i = i + 1
        
#         else:
#             string_new = string_new + string[i]

#     else:
#         if string[i] == " ":
#             string_new = string_new - string[i+1]

# print(string_new)

# USING WHILE LOOP

# s = ""
# string = "patience is the key!"
# s = s + chr(ord(string[0])-32)
# i = 1
# while ( i < len(string)):
#     if string[i] != " ":
#         s = s + string[i]
#         i = i+1
#     else:
#         s = s + string[i]    #push blank
#         s = s + chr(ord(string[i+1])-32)
#         i = i + 2

# print(s)

print(string.ascii_letters)










    

