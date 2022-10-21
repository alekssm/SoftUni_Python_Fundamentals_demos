def valid (index, list_1):
    if 0 <= index < len(list_1):
        return True
    else:
        return False


def shoot (index, power, list_1):
    if valid(index, list_1):
        list_1[index] -= power
        if list_1[index] <= 0:
            list_1.pop(index)
    return list_1


def addition (index, power, list_1):
    if not valid (index, list_1):
        print("Invalid placement!")
        return list_1
    else:
        list_1.insert(index,power)
        return list_1


def strike (index, power, list_1):
    left_index = index - power
    right_index = index + power
    if valid(index, list_1) and valid (left_index, list_1) and (right_index, list_1):
        #for ind in range (left_index, right_index + 1):
            #list_1.pop(left_index)
        del list_1[left_index:right_index + 1]

        return list_1

    else:
        print("Strike missed!")

        return list_1


all_the_targets = list(map(int, input().split()))

command = input()

while not command == "End":
    action, ind, value = command.split()
    ind = int(ind)
    value = int(value)
    if action == "Shoot":
        all_the_targets == shoot(ind, value, all_the_targets)
    elif action == "Add":
        all_the_targets == addition(ind, value, all_the_targets)
    elif action == "Strike":
        all_the_targets == strike(ind, value, all_the_targets)

    command = input()

print("|".join(list(map(str, all_the_targets))))