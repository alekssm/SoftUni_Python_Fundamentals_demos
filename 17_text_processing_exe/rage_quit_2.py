text = input()

final = ""

curr_res = ""

for ch in text:
    if not ch.isdigit():
        curr_res += ch
    else:
        curr_res = curr_res.upper()*int(ch)
        final += curr_res
        curr_res = ""

print(f"Unique symbols used: {len(set(final))}")
print(final)