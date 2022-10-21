list_of_happiness = [int(el) for el in input().split()]
willy = int(input())

list_of_happiness = [ele*willy for ele in list_of_happiness]

meter_for_happiness = sum(list_of_happiness) / len(list_of_happiness)

happy_people_num = len([elem for elem in list_of_happiness if elem >= meter_for_happiness])

if happy_people_num < len(list_of_happiness) / 2:
    print(f"Score: {happy_people_num}/{len(list_of_happiness)}. Employees are not happy!")
else:
    print(f"Score: {happy_people_num}/{len(list_of_happiness)}. Employees are happy!")