students = {}
submissions = {}

while True:
    info = input().split("-")
    if info[0] == "exam finished":
        break

    if len(info) == 3:
        student = info[0]
        lang = info[1]
        points = int(info[2])

        if student not in students:
            students[student] = points
        else:
            if points > students[student]:
                students[student] = points

        if lang not in submissions:
            submissions[lang] = 0
        submissions[lang] += 1

    elif len(info) == 2:
        student = info[0]

        if student in students:
            students.pop(student)

print("Results:")
for (k, v) in sorted(students.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{k} | {v}")

print("Submissions:")
for (k, v) in sorted(submissions.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{k} - {v}")
