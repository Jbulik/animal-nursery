# Класс pack_animals

from animals.animal import Animal



class PackAnimals(Animal):
    def __init__(self, animal_id, name, species, birth_date, commands):
        super().__init__(animal_id, name, birth_date)
        self.species = species
        self.commands = commands

    def list_commands(self):
        return self.commands

    def learn_command(self, new_command):
        self.commands.append(new_command)
