from functools import reduce
student_marks = {}
n = int(input())
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
for i in student_marks:
    if i == query_name:
        lines = student_marks[i]
        total = sum(lines)
        print(total)
        print("{:.2f}".format(total / len(lines)))
