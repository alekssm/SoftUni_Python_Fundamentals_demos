num = int(input())

dictionary = {}

for _ in range(num):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for key in dictionary:
    print(f"{key} - {', '.join(dictionary[key])}")
