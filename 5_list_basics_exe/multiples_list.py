fac = int(input())
count = int(input())

list_of_multiples = []
counting = 0

while len(list_of_multiples) < count:
    num = fac + counting
    if num % fac == 0:
        list_of_multiples.append(num)
    counting += 1

print(list_of_multiples)