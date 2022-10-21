characters = input()
char = ""
num = ""

for sym in characters:
    if sym.isdigit():
        num += sym
        characters = characters.replace(sym, "", 1)

for sym in characters:
    if sym.isalpha():
        char += sym
        characters = characters.replace(sym, "", 1)

print(num)
print(char)
print(characters)