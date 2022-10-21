def urgent(item, list_1):
    if item not in list_1:
        list_1.insert(0, item)
    return list_1


def unnecessary(item, list_1):
    if item in list_1:
        list_1.remove(item)
    return list_1


def correct(item_1, item_2, list_1):
    if item_1 in list_1:
        ind = list_1.index(item_1)
        list_1.remove(item_1)
        list_1.insert(ind, item_2)
    return list_1


def rearrange(item, list_1):
    if item in list_1:
        list_1.remove(item)
        list_1.append(item)
    return list_1


shopping_list = input().split("!")
command = input()

while not command == "Go shopping!":
    com_list = command.split()
    act = com_list[0]
    item = com_list[1]
    if len(com_list) == 3:
        item_2 = com_list[2]

    if act == "Urgent":
        urgent(item, shopping_list)
    elif act == "Unnecessary":
        unnecessary(item,shopping_list)
    elif act == "Correct":
        correct(item, item_2, shopping_list)
    elif act == "Rearrange":
        rearrange(item, shopping_list)

    command = input()

print(", ".join(shopping_list))