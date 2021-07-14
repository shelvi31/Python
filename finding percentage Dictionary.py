n = int(input())
student_marks = {}
for _ in range(0,n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print(student_marks)

print ("Dict key-value are : ")
for i in test_dict :
    print(i, test_dict[i])