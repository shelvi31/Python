#to find non overlapping string - only

import re
needle = input()
haystack = input()
repeat = re.findall(needle,haystack)
print(len(repeat))

#this other code also doesnt consider overlap string
string = "GeeksforGeeksforGeeksforGeeks"
print(string.count("GeeksforGeeks")) 

#Considering Overlapped strings