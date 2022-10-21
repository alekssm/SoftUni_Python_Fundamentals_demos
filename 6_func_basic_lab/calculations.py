def calculate_the_result(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2

calculate = input()
number_1 = int(input())
number_2 = int(input())

print(calculate_the_result(calculate, number_1, number_2))