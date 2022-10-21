information = input()

courses = {}

while ":" in information:
    name, student_id, course = information.split(":")
    if course not in courses: #създаваме праззен лист, с ключ името на курса
        courses[course] = {} #стойността е този празен лист
    courses[course][student_id] = name #този празен лист се попълва с ключ и стойност
    information = input()

searched_course = information.split("_")
searched_course_reforged = " ".join(searched_course)

if searched_course_reforged in courses:
    for id, name in courses[searched_course_reforged].items():
        print(f"{name} - {id}")
