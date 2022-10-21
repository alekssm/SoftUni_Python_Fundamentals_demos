def password_validator_func(password):
    password_val_check = True
    if 6 > len(password) or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        password_val_check = False

    no_char_in = True
    for char in password:
        if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            pass
        else:
            no_char_in = False
    if not no_char_in:
        print("Password must consist only of letters and digits")
        password_val_check = False

    num_of_digits = 0
    for symb in password:
        if 48 <= ord(symb) <= 57:
            num_of_digits += 1
    if num_of_digits < 2:
        print("Password must have at least 2 digits")
        password_val_check = False

    if password_val_check:
        print("Password is valid")

password = input()

password_validator_func(password)