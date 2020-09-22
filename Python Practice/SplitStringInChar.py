#Split string into list of characters

#Using for loop

import string
# alphabet = string.ascii_uppercase
# def split(word):
#     return [char for char in word]

# x = split(alphabet)
# print(x)

#0R

#Using Typecasting to list
alphabet = string.ascii_uppercase
def split(word):
    return (list(word))

print(split(alphabet))


