text = input().split(", ")

for word in text:
    is_valid = True
    if len(word) < 3 or len(word) > 16:
        is_valid = False
    for let in word:
        if let.isdigit() or let.isalpha() or let == "_" or let == "-":
            pass
        else:
            is_valid = False
    stripped = word.strip()
    if not len(word) == len(stripped):
        is_valid = False
    if is_valid:
        print(word)