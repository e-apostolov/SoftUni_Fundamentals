class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal):
        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fishes.append(animal)
        else:
            self.birds.append(animal)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        else:
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {self.__animals}"
        return result



zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())


for line in range(n):
    command = input().split()
    species, animal = command[0], command[1]
    zoo.add_animal(species, animal)


info = input()
print(zoo.get_info(info))







