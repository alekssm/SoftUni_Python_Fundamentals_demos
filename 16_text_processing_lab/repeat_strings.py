words = input().split()

res = ""

for word in words:
    res += word * len(word)

print(res)