#Create a function that converts a string of letters to their respective number in the alphabet

import string
def split(word):
    return (list(word))

alphabet = split(string.ascii_uppercase)


dict = {}
for i in range(0,26):
    dict[i] = alphabet[i]

txt = "XYZ"
A = split(txt)

rev_dict = {value : key for (key, value) in dict.items()}
print(rev_dict)

for i in range(0,len(A)):
    print(rev_dict.get(A[i]))




