list_of_income = input().split(", ")
num_of_beggars = int(input())

list_of_int = list(map(int, list_of_income))

the_final_list = [0]*num_of_beggars

for i in range(len(list_of_int)):
    index = i % num_of_beggars
    the_final_list[index] += list_of_int[i]

print(the_final_list)