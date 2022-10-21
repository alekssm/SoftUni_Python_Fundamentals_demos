def collect(item, list_1):
    if item not in list_1:
        list_1.append(item)
    return list_1

def drop(item, list):
    if item in list:
        list.remove(item)
    return list

def renew (item,list):
    if item in list:
        list.remove(item)
        list.append(item)
    return list

def combine(items, list):
    item_old, item_new = items.split(":")
    if item_old in list:
        list.insert(list.index(item_old)+1, item_new)
    return list

list_of_items = input().split(", ")

command = input()

while not command == "Craft!":
    com_list = command.split(" - ")
    item = com_list[1]
    if com_list[0] == "Collect":
        collect(item, list_of_items)
    elif com_list[0] == "Drop":
        drop(item, list_of_items)
    elif com_list[0] == "Combine Items":
        combine(item, list_of_items)
    elif com_list[0] == "Renew":
        renew(item, list_of_items)
    command = input()

print(", ".join(list_of_items))