deck = input().split(" ")
num_of_shuffles = int(input())

half_deck_size = len(deck) // 2
for shuffle in range (num_of_shuffles):

    first_deck_side = deck[0:half_deck_size]
    second_deck_side = deck[half_deck_size:len(deck)]

    faro_shuffle_deck = []

    for index in range (len(first_deck_side)):
        faro_shuffle_deck.append(first_deck_side[index])
        faro_shuffle_deck.append(second_deck_side[index])
    deck = faro_shuffle_deck

print(deck)