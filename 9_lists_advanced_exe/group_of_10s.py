the_given_numbers = list(map(int, input().split(", ")))
num_of_groups = 10
current_list = []

while not len(the_given_numbers) == 0:
    grp = [ele for ele in the_given_numbers if ele <= num_of_groups]
    for ele in grp:
        the_given_numbers.remove(ele)
    print(f"Group of {num_of_groups}'s: {grp}")
    num_of_groups += 10