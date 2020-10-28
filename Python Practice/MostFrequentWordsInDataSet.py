from collections import Counter
p = ""
while True:
    poem = input()
    if poem == "###":
        break
    p = p + " " + poem
    p1 = p.lower()

words = p1.split()
word_counts = Counter(words)
frequent = word_counts.most_common(1)
print(frequent[0][0])

