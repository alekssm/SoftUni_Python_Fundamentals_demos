divisor = int(input())
bound = int(input())
num_max = 0
for num in range (divisor, bound + 1):
    if num % divisor == 0:
        num_max = num
print(num_max)