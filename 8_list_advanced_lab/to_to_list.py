notes = [0] * 10

note = input()

while not note == "End":
    importance, task = note.split("-")
    notes[int(importance)-1] = task

    note = input()

print([x for x in notes if not x == 0])