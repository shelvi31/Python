#Write a function getBASIC() which takes no arguments, and does the following:
#  it should keep reading lines from input using a while loop; 
# when it reaches the end it should return the whole program in the form of a list of strings. 

def getBASIC():
    list = []
    while True:  
        s = input()
        list.append(s)
        if s.endswith("END"):
            break
    return list

print(getBASIC())