def result_of_even_and_odd(num):
    sum_of_even = 0
    sum_of_odd = 0

    for char in num:
        if int(char) % 2 == 0:
            sum_of_even += int(char)
        else:
            sum_of_odd += int(char)
    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


number = input()

print(result_of_even_and_odd(number))