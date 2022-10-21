n = int(input())
word = input()

all_of_it = []
filtered_words_list = []

for _ in range (n):
    the_current_string = input()
    all_of_it.append(the_current_string)
    if word in the_current_string:
        filtered_words_list.append(the_current_string)

print(all_of_it)
print(filtered_words_list)