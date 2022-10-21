def remove(list_1, cho, numbers):
    if cho == "first":
        for _ in range(numbers):
            list_1.pop(0)
    elif cho == "last":
        for _ in range(numbers):
            list_1.pop(-1)


coffees = input().split()
num = int(input())

for _ in range(num):
    command = input().split()
    if command[0] == "Reverse":
        coffees.reverse()
    elif command[0] == "Include":
        coffees.append(command[1])
    elif command[0] == "Remove":
        choice = command[1]
        number = int(command[2])
        remove(coffees, choice, number)
    elif command[0] == "Prefer":
        first = int(command[1])
        second = int(command[2])
        if first < len(coffees) and second < len(coffees):
            coffees[first], coffees[second] = coffees[second], coffees[first]

print("Coffees:")
print(f"{' '.join(coffees)}")