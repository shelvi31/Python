# def ceaser(s,x):
#     s1 = ""
#     for letter in s:
#         y = ord(letter) + x
#         if y < ord("Z") and y > ord("A"):
#             new_letter = chr(ord(letter)+x)
#             if letter == " ":
#                 s1 = s1 + letter
#             else:
#                 s1 = s1 + new_letter
#         else:
#             if y > ord("Z"):
#                 d = ord("Z") - ord(letter)
#                 new_letter = chr(ord("A")+ x -d)
#                 if letter == " ":
#                     s1 = s1 + letter
#                 else:
#                     s1 = s1 + new_letter
#             if y < ord("A"):
#                 d = ord(letter)- ord("A") 
#                 new_letter = chr(ord("Z") -x + d )
#                 if letter == " ":
#                     s1 = s1 + letter
#                 else:
#                     s1 = s1 + new_letter
#     return s1


# print(ceaser("SPY CODER",5))

prog = ['10 GOTO 20', '20 END']
s1 = prog[0].split(" ")
print(s1)
s2 = prog[1].split(" ")
print(s2)
s = (s1 + s2)
print(s)
print("".join(str(prog).split()))
 