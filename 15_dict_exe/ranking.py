cont_pass = {} # dict of available contents and the pass for them

while True:
    info = input()
    if info == "end of contests":
        break

    cont, pas = info.split(":")
    cont_pass[cont] = pas

users = {}

while True:
    info = input()
    if info == "end of submissions":
        break

    cont, pas, user, points = info.split("=>")

    if cont in cont_pass:
        if cont_pass[cont] == pas:
            if user not in users:
                users[user] = {}
                users[user][cont] = int(points)
            else:
                if cont not in users[user]:
                    users[user][cont] = int(points)
                else:
                    if int(points) > users[user][cont]:
                        users[user][cont] = int(points)

max_result = 0
best_user = ''

for user in users:
    max_points = 0

    for y in users[user]:
        max_points += users[user][y]

    if max_points > max_result:
        max_result = max_points
        best_user = user

print(f"Best candidate is {best_user} with total {max_result} points.")

for (k, v) in sorted(users.items(), key=lambda kvp: kvp[0]):
    print(k)

    for (cont, point) in sorted(v.items(), key=lambda kvp: -kvp[1]):
        print(f"{cont}->{point}")
