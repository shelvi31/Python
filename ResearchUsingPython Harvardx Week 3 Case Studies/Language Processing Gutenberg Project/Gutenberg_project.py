# # Counting Words in Book using self made counting function

text = "Hi, this is Shelvi Garg. Nice to meet you. This code is written by Shelvi. "
def count_words(text):
    """Count the number of times each word occurs in text. Show number count in dictionary.Skip punctuation.Lower case"""  #adding docstring to function
    text = text.lower()
    skips = [".",",", ":", ";","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = {}
    for word in text.split(" "):          #splitted the words with blanks and do a loop over loop
        if word in word_counts:
            word_counts[word] += 1     # +1 if word is getting repeted
        else:
            word_counts[word] = 1
    return word_counts

# print(count_words(text))


# Counting Words using counter function

from collections import Counter
text = "Hi, this is Shelvi Garg. Nice to meet you. This code is written by Shelvi. "

def count_words_fast(text):
    """Count the number of times each word occurs in text. Show number count in dictionary.Skip punctuation.Lower case"""  #adding docstring to function
    text = text.lower()
    skips = [".",",", ":", ";","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = Counter(text.split(" "))
    return word_counts

# print(count_words_fast(text))
# print(count_words_fast(text) == count_words(text))       #True but now faster

#Comprehension Check Question
# print(len(count_words("This comprehension check is to check for comprehension.")))
# print(count_words(text) is count_words_fast(text))                  #While the two provide the same results, they are different objects in memory.


# READING THE BOOK

def read_book(title_path):              #the input argument requires path of the title of the book
    """Read a book and return it as a string"""
    with open(title_path,"r",encoding = "utf8") as current_file:            #we will use encoding utf8
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

# text = read_book("C:/Users/Shelvi Garg/Desktop/Romeo and Juliet.txt")     #inputting location of downloaded utf8 file from gutenberg site
# print(len(text1))

# ind = text.find("in a name")        #using find method
# print(ind)

# sample_text = text1[ind : ind +1000]
# print(sample_text)


# Computing Word Frequency Statistics

def word_stats(word_counts):
    """ return number of unique words and word frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique,counts)


#text = read_book("C:/Users/Shelvi Garg/Desktop/Romeo and Juliet.txt")
word_counts = count_words(text)

(num_unique,counts) = word_stats(word_counts)

print(num_unique)
print(sum(counts))                  #total number of words


#Reading Multiple Files

import os
book_dir = ("C:/Users/Shelvi Garg/Desktop/BooksPython")
print(os.listdir(book_dir))          #We first want to generate a list of the directories that are contained within our "Books" directory
#Since these directories will correspond to different languages,gonna call the loop variable language

import pandas as pd
stats = pd.DataFrame( columns = ("language", "author","title", "length","unique"))   #table with these 5 coloumns
title_num = 1 

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):   # we need to add the new directory that we're currently in which is the language. We can do this by concatenating strings.
        for title in os.listdir(book_dir + "/" + language + "/" + author):   #our first for loop is looping over languages.The second for loop is looping over authors.And the third, the innermost for loop, is loopingover different titles, different books.
            input_file = book_dir + "/" + language + "/" + author + "/" + title
            text = read_book(input_file)
            stats.loc[title_num] = language , author.capitalize() , title.replace(".txt","") , sum(counts) , num_unique
            title_num += 1
            (num_unique, counts) = word_stats(count_words(text))

# print(stats)        
# print(stats.head)
# print(stats.tail)

import matplotlib.pyplot as plt

plt.plot(stats.length, stats.unique, "bo")
# plt.show()
# plt.savefig("plot1".pdf")
plt.loglog(stats.length, stats.unique, "bo")
# plt.savefig("plot2.pdf")

#Let's construct a plot using different colors for different languages.
plt.figure(figsize = (10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length,subset.unique,"o",label = "English",color = "crimson")

subset = stats[stats.language == "French"]
plt.loglog(subset.length,subset.unique,"o",label = "French",color = "orange")

subset = stats[stats.language == "German"]
plt.loglog(subset.length,subset.unique,"o",label = "German",color = "forestgreen")

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length,subset.unique,"o",label = "Portuguese",color = "blueviolet")

plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of unique words")
# plt.savefig("language_plot.pdf")
plt.show()


#TASK ACCOMPLISHED :

# 1) Counting words frequency in books.
# 2)Navigate file directories
# 3) Using Counter Functions using Collections Module
# 4) Basic Pandas