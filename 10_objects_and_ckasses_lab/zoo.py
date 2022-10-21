class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        if species == "bird":
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == "fish":
            return f'Fishes in {self.name}: {", ".join(self.fishes)}'
        if species == "bird":
            return f'Birds in {self.name}: {", ".join(self.mammals)}'


    def get_count(self):
        return self.__animals


name = input()
zoo = Zoo(name)
num = int(input())

for n in range (num):
    species, animal_name = input().split()
    zoo.add_animal(species, animal_name)

choose_species = input()
print(zoo.get_info(choose_species))
print(f"Total animals: {zoo.get_count()}")
