def perfect_num_finder(num):
    list_of_num_del = []

    for digit in range(1, num):
        if num % digit == 0:
            list_of_num_del.append(digit)
    if sum(list_of_num_del) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())

print(perfect_num_finder(num))