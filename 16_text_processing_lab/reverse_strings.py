words = input()

while words != "end":
    print(f"{words} = {words[::-1]}")

    words = input()