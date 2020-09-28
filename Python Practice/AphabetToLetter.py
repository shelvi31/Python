#CONVERT NUMBERS TO LETTERS 

x = int(input())
if x>=1 and x<=26:
    print('letter', x, 'in the alphabet:', chr(ord('A')+(x-1)))
else:
    print('invalid input:', x)


#CONVERT ALPHABET TO NUMBERS

letter = input()
if letter >="A" and letter <="Z":
   print(ord(letter) - ord("A") + 1)
else:
   print("invalid")
   