num = int(input())
sum_of_digits = 0

for digit in range (1, num + 1):
    str_num = str(digit)
    for index in range (len(str_num)):
        sum_of_digits += int(str_num[index])
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{digit} -> True")
    else:
        print(f"{digit} -> False")
    sum_of_digits = 0