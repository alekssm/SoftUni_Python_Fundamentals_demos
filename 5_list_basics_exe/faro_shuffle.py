deck = input().split(" ")
num_of_shuffles = int(input())

first_side = []
second_side = []

for shuffle in range (num_of_shuffles):

    while len(deck) >= len(deck)/2:
        for element in deck:
            first_side.append(element)
            deck.remove(element)
        second_side = deck
        deck = first_side + second_side

print(deck)