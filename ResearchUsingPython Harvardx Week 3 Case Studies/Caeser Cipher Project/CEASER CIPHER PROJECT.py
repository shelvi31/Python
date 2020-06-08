import string
alphabet = " " + string.ascii_lowercase
print(alphabet)


positions = {}
index = 0
for char in alphabet:
    positions[char] = index
    index += 1
print(positions)


# encoding_list = []
# for char in message:
#     position = positions[char]
#     encoded_position = (position + 1) % 27             #ensure the result remains within 0-26 using result % 27
#     encoding_list.append(alphabet[encoded_position])
# encoded_message = "".join(encoding_list)
# print(encoded_message)

key = int
def encoding(message,key):
    message = "hi my name is caesar"
    encoding_message = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27             #ensure the result remains within 0-26 using result % 27
        encoding_message.append(alphabet[encoded_position])
    # encoded_message = "".join(encoding_list)
    return(encoded_message)

message = "hi my name is caesar"
encoded_message = encoding(message,3)
decoded_message = encoding(encoded_message, -3)
print(decoded_message)
print(encoded_message)
