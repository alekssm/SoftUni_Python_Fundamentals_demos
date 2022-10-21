n = int(input())

plus_list = []
minus_list = []

for _ in range (n):
    num = int(input())
    if num >= 0:
        plus_list.append(num)
    else:
        minus_list.append(num)

print(plus_list)
print(minus_list)
print(f"Count of positives: {len(plus_list)}. Sum of negatives: {sum(minus_list)}")