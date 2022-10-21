list_of_num = input().split(", ")
#int_of_num = list(map(int, list_of_num))
int_of_num = [int(x) for x in list_of_num]

even_index_list = [index for index in range (len(int_of_num)) if int_of_num[index] % 2 == 0]

print(even_index_list)