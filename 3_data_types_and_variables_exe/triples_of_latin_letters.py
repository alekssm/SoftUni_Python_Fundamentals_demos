n = int(input())

for i in range (n):
    for m in range(n):
        for p in range(n):
            print(f"{chr(97+i)}{chr(97+m)}{chr(97+p)}")