cards = input()

list_of_cards_not_set = cards.split(" ")
a_team_count = 11
b_team_count = 11

list_of_cards = set(list_of_cards_not_set)

for element in list_of_cards:
    if "A" in element:
        a_team_count -= 1
    else:
        b_team_count -= 1

print(f"Team A - {a_team_count}; Team B - {b_team_count}")
if a_team_count < 7 or b_team_count < 7:
    print("Game was terminated")