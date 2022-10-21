str1 = input()
str2 = input()
last_string = str1

for symbol in range (len(str1)):
    left_part = str2[:symbol+1]
    right_part = str1[symbol+1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string