text = input()

occurrences = {}

for ch in text:
    if ch == ' ':
        continue
    if ch not in occurrences:
        occurrences[ch] = 0
    occurrences[ch] += 1

for k, v in occurrences.items():
    print(f"{k} -> {v}")
