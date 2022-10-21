team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input().split(" ")

finished = False

for element in cards:
    card_info_given = element.split("-")

    card_team = card_info_given[0]
    card_number = int(card_info_given[1])

    if card_team == "A" and card_number in team_a:
        team_a.remove(card_number)
    elif card_team == "B" and card_number in team_b:
        team_b.remove(card_number)

    if len(team_a) <= 6 or len(team_b) <= 6:
        finished = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if finished:
    print("Game was terminated")