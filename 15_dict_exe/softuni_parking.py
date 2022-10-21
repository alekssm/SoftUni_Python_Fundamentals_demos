num = int(input())

registered_users = {}

for n in range(num):
    command = input().split()

    action = command[0]
    user = command[1]

    if action == "register":
        plate_number = command[2]

        if user not in registered_users:
            registered_users[user] = plate_number
            print(f"{user} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_users[user]}")

    elif action == "unregister":
        if user not in registered_users:
            print(f"ERROR: user {user} not found")
        else:
            registered_users.pop(user)
            print(f"{user} unregistered successfully")

for k, v in registered_users.items():
    print(f"{k} => {v}")
