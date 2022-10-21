class Party:
    def __init__(self):
        self.people = []

parties = Party()


ppl = input()
while not ppl == "End":
    parties.people.append(ppl)
    ppl = input()

print(f"Going: {', '.join(parties.people)}")
print(f"Total: {len(parties.people)}")