# класс для реестра животных

from animals.pets import Pets

from animals.pack_animals import PackAnimals


class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals_by_birth_date(self):
        sorted_animals = sorted(self.animals, key=lambda x: x.birth_date)
        for animal in sorted_animals:
            print(f"{animal.name}: {animal.birth_date}")

    def list_animals_by_group(self, group):
        if group.lower() == 'pets':
            pets = [animal for animal in self.animals if isinstance(animal, Pets)]
            for pet in pets:
                print(f"{pet.name}: {pet.species}")
        elif group.lower() == 'packanimals':
            pack_animals = [animal for animal in self.animals if isinstance(animal, PackAnimals)]
            for pack_animal in pack_animals:
                print(f"{pack_animal.name}: {pack_animal.species}")
        else:
            print("Некорректная группа.")

    def total_animals(self):
        return len(self.animals)
