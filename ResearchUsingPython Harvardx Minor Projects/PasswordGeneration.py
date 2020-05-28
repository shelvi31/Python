
# PASSWORD GENERATOR

import random
def password(length):
    pw = ""      # can also use pw = str()
    characters = "addfdjfhretzxqpomn" + "1234567890"
    for i in range(length):
        pw = pw + random.choice(characters)
    return(pw)

print(password(5))
print(password(5))

print(password(8))