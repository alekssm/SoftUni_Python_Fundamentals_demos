list_of_numb = input().split(", ")
list_of_int = [int(ele) for ele in list_of_numb]

# Не става зарди непълни списъци

list_of_positive = [ele for ele in list_of_int if not ele < 0]
list_of_negative = [ele for ele in list_of_int if ele < 0]
list_of_even = [ele for ele in list_of_int if ele % 2 == 0]
list_of_odd = [ele for ele in list_of_int if not ele % 2 == 0]

print("Positive: ", end = "")
for x in range (len(list_of_positive) - 1):
    print(list_of_positive[x], end = ", ")
print(list_of_positive[-1])

print("Negative: ", end = "")
for x in range (len(list_of_negative) - 1):
    print(list_of_negative[x], end = ", ")
print(list_of_negative[-1])

print("Even: ", end = "")
for x in range (len(list_of_even) - 1):
    print(list_of_even[x], end = ", ")
print(list_of_even[-1])

print("Odd: ", end = "")
for x in range (len(list_of_odd) - 1):
    print(list_of_odd[x], end = ", ")
print(list_of_odd[-1])