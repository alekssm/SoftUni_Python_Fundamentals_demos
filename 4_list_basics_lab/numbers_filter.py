num = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(num):
    number = int(input())
    if number == 0:
        even.append(number)
        positive.append(number)
    else:
        if number > 0:
            positive.append(number)
        else:
            negative.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)