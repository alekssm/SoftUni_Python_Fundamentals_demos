import sys

num = int(input())

for year in range (num, sys.maxsize, 1):
    num4 = year % 10
    num3 = year // 10 % 10
    num2 = year // 100 % 10
    num1 = year // 1000
    if num1 != num2 and num1 != num3 and num1 != num4 and num3 != num2 and num2 != num4 and num3 != num4:
        print(year)
        print(f"{num1}, {num2}, {num3}, {num4}")
        break