coffees = input().split()

command = input().split()
if command[0] == "Remove":
    choice = command[1]
    number = int(command[2])
    if choice == "first":
        for _ in range(number):
            coffees.pop(0)
    elif choice == "last":
        for _ in range(number):
            coffees.pop(-1)

print(coffees)

