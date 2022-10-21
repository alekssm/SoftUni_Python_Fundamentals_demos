courses = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break

    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        if student_name not in courses[course_name]:
            courses[course_name].append(student_name)

for (k, v) in sorted(courses.items(), key=lambda kvp: len(kvp[1]), reverse=True):
    print(f"{k}: {len(v)}")

    for user in sorted(v):
        print(f"-- {user}")
