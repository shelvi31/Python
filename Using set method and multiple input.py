#Ques: Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

#Input Format : The first line contains n.
# The second line contains an array A[] of integers n each separated by a space.

# Solution : 
n = int(input())
arr = map(int, input().split())      #map(function, iter) : syntax
print(sorted(set(arr)) [-2])


#MAP FUNCTION:
#map() function returns a map object(which is an iterator) 
#of the results after applying the given function to each item of a given iterable(list, tuple etc)


# About Set method:
#set() method is used to convert any of the iterable to sequence of iterable elements
#  with distinct elements, commonly called Set. 
#  -- Return unordered yet unique elements