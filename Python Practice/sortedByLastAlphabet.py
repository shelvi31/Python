def reverse_word(word):
    return word[::-1]

words = ['banana', 'pie', 'Washington', 'book']
print(sorted(words,key = reverse_word))
