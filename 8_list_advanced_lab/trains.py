num = int(input())
wagons = [0] * num

command = input()

while not command == "End":
    action = command.split()
    if "add" in action:
        wagons[-1] += int(action[1])
    elif "insert" in action:
        index = int(action[1])
        people = int(action[2])
        wagons[index] += people
    elif "leave" in action:
        index = int(action[1])
        people = int(action[2])
        wagons[index] -= people
    command = input()

print(wagons)