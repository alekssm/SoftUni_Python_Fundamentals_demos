def sum_numbers(n_1, n_2):
    addition = n_1 + n_2
    return addition


def subtract(sum_1, n_3):
    result = sum_1 - n_3
    return result


def add_and_subtract(n_1, n_2, n_3):
    sum = sum_numbers(n_1, n_2)
    result = subtract(sum, n_3)
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
