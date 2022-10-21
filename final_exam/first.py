def reverse(user, index_1, index_2):
    #if index_1 > len(user)-1 or index_2 > len(user)-1:
    if 0 <= index_1 < len(user) and 0 <= index_2 < len(user):
        splited = user[index_1:index_2+1]
        splited = splited[::-1]
        print(splited)


username = input()

command = input()

while not command == "Sign up":
    split_com = command.split()
    if split_com[0] == "Case":
        choice = split_com[1]
        if choice == "lower":
            username = username.lower()
            print(username)
        elif choice == "upper":
            username = username.upper()
            print(username)
    elif split_com[0] == "Reverse":
        ind_1 = int(split_com[1])
        ind_2 = int(split_com[2])
        reverse(username, ind_1, ind_2)
    elif split_com[0] == "Cut":
        word = split_com[1]
        if word in username:
            print(username.replace(word, ""))
        else:
            print(f"The word {username} doesn't contain {word}.")
    elif split_com[0] == "Replace":
        ch = split_com[1]
        username = username.replace(ch, "*")
        print(username)
    elif split_com[0] == "Check":
        character = split_com[1]
        if character in username:
            print("Valid")
        else:
            print(f"Your username must contain {character}.")

    command = input()