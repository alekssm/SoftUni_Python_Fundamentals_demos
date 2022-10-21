import math
import sys

list_of_num = input().split(" ")
num_to_remove = int(input())

list_of_int = list(map(int, list_of_num))
min_num = sys.maxsize
for _ in range (num_to_remove):
    for element in list_of_int:
        if element < min_num:
            min_num = element
    list_of_int.remove(min_num)
    min_num = sys.maxsize

print(", ".join(map(str, list_of_int)))