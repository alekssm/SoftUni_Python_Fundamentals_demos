text = input().lower()

final = ""

ind = 0
curr_text = ""

while ind < len(text):
    if not text[ind].isdigit():
        curr_text += text[ind]
        ind += 1
    elif text[ind].isdigit():
        number = ""
        while ind < len(text) and text[ind].isdigit():
            number += text[ind]
            ind += 1
        number = int(number)
        final += curr_text.upper()*number
        curr_text = ""

final += curr_text.upper()
print(f"Unique symbols used: {len(set(final))}")
print(final)