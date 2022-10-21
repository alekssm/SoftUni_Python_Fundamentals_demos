def return_the_char(ch_1, ch_2):
    value_1 = ord(ch_1)
    value_2 = ord(ch_2)
    for char_1 in range(value_1 + 1, value_2):
        print(chr(char_1), end = " ")


char_1 = input()
char_2 = input()

return_the_char(char_1, char_2)