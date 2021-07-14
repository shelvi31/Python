# #taking number of students input:
# n = int(input())

# list = []
# for i in range(0,n):
#     t = input().split()
#     list.append(t)
# print(list)

# nested = []
# [ nested.append (tuple( [ list[n-1], list[n] ] )) for n in range(1,len(list),2)]

# sort = sorted(list)
# score = sort[1]

# name = [nested[n][0] for n in range(len(nested)) if nested[n][1]== score]
# name = sorted(name)

# for n in range(len(name)):
#     print((name[n][0]))

#Optimised way for input: 

# marksheet = []
# for i in range(0,int(input)):
#     marksheet.append([input(),float(input())])


#Correct solution:
n = int(input())
list = []
scores = set()
for i in range(0,n):
    name = input()
    score = float(input())
    list.append([name,score])
    scores.add(score)

second_lowest_score = sorted(scores)[1]

name = [list[n][0] for n in range(len(list)) if list[n][1]== second_lowest_score]
name = sorted(name)


for n in range(len(name)):
    print((name[n])) 







