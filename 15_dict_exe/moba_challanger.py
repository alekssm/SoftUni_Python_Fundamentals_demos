players = {}

while True:
    info = input()
    if info == "Season end":
        break

    if "->" in info:
        info_ll = info.split(" -> ")
        player = info_ll[0]
        position = info_ll[1]
        skill = int(info_ll[2])

        if player not in players:
            players[player] = {}
            players[player][position] = skill

        else:
            if position not in players[player]:
                players[player][position] = skill
            else:
                if skill > players[player][position]:
                    players[player][position] = skill

    elif " vs " in info:
        info_ll = info.split(" vs ")
        player_1 = info_ll[0]
        player_2 = info_ll[1]

        if player_1 not in players or player_2 not in players:
            continue

        player_1_positions = list(players[player_1].keys())
        player_2_positions = list(players[player_2].keys())

        common_positions = [x for x in player_1_positions if x in player_2_positions]

        if common_positions:
            player_1_total_score = sum(players[player_1].values())
            player_2_total_score = sum(players[player_2].values())

            if player_1_total_score > player_2_total_score:
                players.pop(player_2)
            elif player_2_total_score > player_1_total_score:
                players.pop(player_1)

for (k, v) in sorted(players.items(), key=lambda kvp: (-sum(kvp[1].values()), kvp[0])):
    print(f"{k}: {sum(v.values())} skill")
    for (m, n) in sorted(v.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"- {m} <::> {n}")
