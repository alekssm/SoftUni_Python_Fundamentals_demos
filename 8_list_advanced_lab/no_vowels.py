word = input()
vow = ["a", "e", "i", "u", "o"]

print("".join([x for x in word if x.lower() not in vow]))