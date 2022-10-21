text = input()

new_text = ""
ind = 0
powa = 0
while ind < len(text):
    symb = text[ind]
    if symb != ">":
        new_text += symb
    else:
        new_text += ">"
        powa += int(text[ind+1])

        while powa > 0:
            ind += 1

            if ind >= len(text):
                break
            symb = text[ind]
            if symb == ">":
                new_text += ">"
                powa += int(text[ind + 1])
            else:
                powa -= 1
    ind += 1

print(new_text)
