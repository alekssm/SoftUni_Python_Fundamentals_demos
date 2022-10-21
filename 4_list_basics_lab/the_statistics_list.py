n = int(input())

plus_list = []
minus_list = []
plus_num_count = 0
minus_num_sum = 0

for _ in range (n):
    num = int(input())
    if num >= 0:
        plus_list.append(num)
        plus_num_count += 1
    else:
        minus_list.append(num)
        minus_num_sum += num

print(plus_list)
print(minus_list)
print(f"Count of positives: {plus_num_count}. Sum of negatives: {minus_num_sum}")