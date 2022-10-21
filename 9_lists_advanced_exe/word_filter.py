list_of_examples = input().split()
list_of_even = [ele for ele in list_of_examples if len(ele) % 2 == 0]

for ele in list_of_even:
    print(ele)