num_of_rooms = int(input())
enough_chairs_everywhere = True
free_chairs = 0
for room in range(1, num_of_rooms + 1):
    chairs, people = input().split()
    people = int(people)
    diff = len(chairs) - people
    if diff >= 0:
        free_chairs += diff
    else:
        enough_chairs_everywhere = False
        free_chairs -= diff
        print(f"{abs(diff)} more chairs needed in room {room}")

if enough_chairs_everywhere:
    print(f"Game On, {free_chairs} free chairs left")