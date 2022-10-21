secret_message = input().split()

for ele in secret_message:
    numbers = ""
    char = []
    for ch in ele:
        if ch.isnumeric():
            numbers += ch
        else:
            char.append(ch)
    char[0], char[-1] = char[-1], char[0]
    char.insert(0, chr(int(numbers)))
    print("".join(char), end = " ")