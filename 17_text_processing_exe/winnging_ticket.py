tickets = input().split(", ")

winning_symbs = ["@", "^", "$", "#"]

for t in tickets:
    ticket = t.strip()
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if len(set(ticket)) == 1 and ticket[0] in winning_symbs:  #(ticket[0] == "$" or ticket[0] == "@" or ticket[0] == "#" or ticket[0] == "^"):
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        else:
            first_half = ticket[:10]
            second_half = ticket[10:]
            symb_no_match = True
            for symb in winning_symbs:
                if symb*6 in first_half and symb*6 in second_half:
                    first_half_match = first_half.count(symb)
                    second_half_match = second_half.count(symb)
                    min_symb_match = min(first_half_match, second_half_match)
                    print(f'ticket "{ticket}" - {min_symb_match}{symb}')
                    symb_no_match = False
                    break
            if symb_no_match:
                print(f'ticket "{ticket}" - no match')
