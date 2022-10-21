list_of_numb = list(map(int, input().split(", ")))
list_of_positive = [str(ele) for ele in list_of_numb if not ele < 0]
list_of_negative = [str(ele) for ele in list_of_numb if ele < 0]
list_of_even = [str(ele) for ele in list_of_numb if ele % 2 == 0]
list_of_odd = [str(ele) for ele in list_of_numb if not ele % 2 == 0]

print(f'Positive: {", ".join(list_of_positive)}')
print(f'Negative: {", ".join(list_of_negative)}')
print(f'Even: {", ".join(list_of_even)}')
print(f'Odd: {", ".join(list_of_odd)}')