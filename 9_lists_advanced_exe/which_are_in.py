list_of_str = input().split(", ")
list_of_words = input()

print([ele for ele in list_of_str if ele in list_of_words])