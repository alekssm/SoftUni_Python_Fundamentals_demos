year_input = int(input())

while True:
    year_input += 1
    year_string = str(year_input)
    if len(year_string) == len(set(year_string)):
        print(year_input)
        break
