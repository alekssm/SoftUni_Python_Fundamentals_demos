import string

text = input().split()

result = 0

for word in text:
    first_letter = word[0]
    last_letter = word[-1]
    num = int(word[1:-1])
    first_letter_number = string.ascii_lowercase.index(first_letter.lower())+1
    last_letter_number = string.ascii_lowercase.index(last_letter.lower())+1
    first_res = 0
    final_res = 0
    if not first_letter.islower():
        first_res = num/first_letter_number
    else:
        first_res = num * first_letter_number

    if not last_letter.islower():
        final_res = first_res - last_letter_number
    else:
        final_res = first_res + last_letter_number
    result += final_res

print(f"{result:.2f}")