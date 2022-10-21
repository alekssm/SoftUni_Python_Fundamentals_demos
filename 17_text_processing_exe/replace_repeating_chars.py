text = input()

new_text = ""

for ind in range(len(text)-1):
    if not text[ind] == text[ind+1]:
        new_text += text[ind]
new_text += text[-1]

print(new_text)