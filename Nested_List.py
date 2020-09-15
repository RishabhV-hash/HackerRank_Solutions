students = []
#store the list
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
#find the second lowest grade
second_low = sorted(set([i[1] for i in students]))[1]
print("\n".join(sorted([i[0] for i in students if i[1] == second_low])))
