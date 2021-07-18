if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()    # * signifies non-fixed no of variable
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

for key,value in student_marks.items():
    if key == query_name:
        su = (sum(value)/len(value))

su = "{:.2f}".format(su)
print(su)


#ALternative Optimized Solution
student_marks = { "malika" : [56,4,21], "arjun" : [90,89,78],"krishna": [98,100,18]}
query_name = "malika"
query_scores = student_marks [query_name]
print("{:.2f}".format(sum(query_scores)/len(query_scores)))
