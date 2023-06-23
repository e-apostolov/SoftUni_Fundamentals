class Party:
    def __init__(self):
        self.people = []

my_party = Party()

while True:
    name = input()

    if name == "End":
        break
    my_party.people.append(name)

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
