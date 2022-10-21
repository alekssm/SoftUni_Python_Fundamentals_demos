n = int(input())

students = {}
current_student = ''


for i in range(1, n*2+1):
    info = input()
    if i % 2 != 0:
        current_student = info
    else:
        if current_student not in students:
            students[current_student] = []
        students[current_student].append(float(info))

students_passed = {student: (sum(students[student])/len(students[student])) for student in students if sum(students[student])/len(students[student]) >= 4.50}
for (k, v) in sorted(students_passed.items(), key=lambda kvp: kvp[1], reverse=True):
    print(f"{k} -> {v:.2f}")
