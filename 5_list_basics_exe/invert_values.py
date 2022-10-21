numbers = input()

list_of_num = numbers.split(" ")
converted_list_num = []

for ind in list_of_num:
    current_num_listed = int(ind) * - 1
    converted_list_num.append(current_num_listed)

print(converted_list_num)