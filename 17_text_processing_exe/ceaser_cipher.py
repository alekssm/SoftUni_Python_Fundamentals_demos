text = input()

encrypted = ""

for ch in text:
    new_char_code = ord(ch) + 3
    encrypted += chr(new_char_code)

print(encrypted)