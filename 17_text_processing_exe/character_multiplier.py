data = input()
word_1, word_2 = data.split()

sum = 0

shorter_word_len = min(len(word_1), len(word_2))

for i in range (shorter_word_len):
    cur_ch_1 = word_1[i]
    cur_ch_2 = word_2[i]

    sum_of_char = ord(cur_ch_1) * ord(cur_ch_2)
    sum += sum_of_char

longer_word_len = max(len(word_1), len(word_2))
for i in range (shorter_word_len, longer_word_len):
    if len(word_1) > len(word_2):
        cur_word_char = word_1[i]
    elif len(word_1) < len(word_2):
        cur_word_char = word_2[i]

    sum += ord(cur_word_char)

print(sum)
