import sys

def exchange(command_1, list_1):
    list_command = command_1.split(" ")
    split_index = int(list_command[1])
    if 0 <= split_index < len(list_1):
        first_side = list_1[0:split_index+1]
        second_side = list_1[split_index+1:]
        second_side.extend(first_side)
        return second_side
    else:
        return "Invalid index"



def max_even_odd(command_1, list_1):
    list_command = command_1.split(" ")
    if list_command[1] == "odd":
        max_int = -sys.maxsize
        max_ind = -sys.maxsize
        for ind in range (0, len(list_1)):
            if not list_1[ind] % 2 == 0:
                if list_1[ind] >= max_int:
                    max_int = list_1[ind]
                    max_ind = ind
        return max_ind
    if list_command[1] == "even":
        max_int = -sys.maxsize
        max_ind = -sys.maxsize
        for ind in range (0, len(list_1)):
            if list_1[ind] % 2 == 0:
                if list_1[ind] >= max_int:
                    max_int = list_1[ind]
                    max_ind = ind
        return max_ind



def min_even_odd(command_1, list_1):
    list_command = command_1.split(" ")
    if list_command[1] == "odd":
        min_int = sys.maxsize
        min_ind = sys.maxsize
        for ind in range (0, len(list_1)):
            if not list_1[ind] % 2 == 0:
                if list_1[ind] <= min_int:
                    min_int = list_1[ind]
                    min_ind = ind
        return min_ind
    elif list_command[1] == "even":
        min_int = sys.maxsize
        min_ind = sys.maxsize
        for ind in range (0, len(list_1)):
            if list_1[ind] % 2 == 0:
                if list_1[ind] <= min_int:
                    min_int = list_1[ind]
                    min_ind = ind
        return min_ind


def first_even_odd (command_1, list_1):
    list_command = command_1.split(" ")
    int_list_1 = list(map(int, list_1))
    new_list = []
    num_of_ele = int(list_command[1])
    if num_of_ele > len(list_1):
        return "Invalid count"
    else:
        if list_command[2] == "even":
            count_of_ele = 0
            for ind in range (0, len(int_list_1)):
                if count_of_ele == num_of_ele:
                    break
                if int_list_1[ind] % 2 == 0:
                    new_list.append(int_list_1[ind])
                    count_of_ele += 1
            return new_list
        if list_command[2] == "odd":
            count_of_ele = 0
            for ind in range (0, len(int_list_1)):
                if count_of_ele == num_of_ele:
                    break
                if not int_list_1[ind] % 2 == 0:
                    new_list.append(int_list_1[ind])
                    count_of_ele += 1
            return new_list

def last_even_odd (command_1, list_1):
    list_command = command_1.split(" ")
    int_list_1 = list(map(int, list_1))
    new_list = []
    num_of_ele = int(list_command[1])
    if num_of_ele > len(list_1):
        return "Invalid count"
    else:
        if list_command[2] == "even":
            count_of_ele = 0
            for ind in range (len(int_list_1) - 1, -1, -1):
                if count_of_ele == num_of_ele:
                    break
                if int_list_1[ind] % 2 == 0:
                    new_list.append(int_list_1[ind])
                    count_of_ele += 1
            return new_list
        if list_command[2] == "odd":
            count_of_ele = 0
            for ind in range (len(int_list_1) -1, - 1, -1):
                if count_of_ele == num_of_ele:
                    break
                if not int_list_1[ind] % 2 == 0:
                    new_list.append(int_list_1[ind])
                    count_of_ele += 1
            return new_list

original_list = input().split(" ")
int_list = list(map(int, original_list))

command = input()

while not command == "end":
    if "exchange" in command:
        print(exchange(command, int_list))
        if exchange(command, int_list) != "Invalid index":
            int_list = exchange(command, int_list)
    elif "max" in command:
        print(max_even_odd(command, int_list))
    elif "min" in command:
        print(min_even_odd(command, int_list))
    elif "first" in command:
        print(first_even_odd(command, int_list))
    elif "last" in command:
        print(last_even_odd(command, int_list))
    command = input()

print(int_list)