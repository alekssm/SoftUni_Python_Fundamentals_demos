def fact_multi_num(num):
    result = num
    if num == 0:
        result = 1
    else:
        for digit in range (num - 1, 0, -1):
            result *= digit
    return result


num_1 = int(input())
num_2 = int(input())

res_1 = fact_multi_num(num_1)
res_2 = fact_multi_num(num_2)

result_of_division = res_1 / res_2
print(f"{result_of_division:.2f}")