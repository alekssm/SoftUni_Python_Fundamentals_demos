n = int(input())

sum = 0

for i in range (1, n + 1):
    char = input()
    char_current_num = ord(char)
    sum += char_current_num

print(f"The sum equals: {sum}")