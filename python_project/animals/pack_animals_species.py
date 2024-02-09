# виды и действия вьючных животных

from pack_animals import PackAnimals

class Horse(PackAnimals):
    def __init__(self, animal_id, name, birth_date):
        super().__init__(animal_id, name, "Horse", birth_date, ["Trot", "Canter", "Gallop"])

class Camel(PackAnimals):
    def __init__(self, animal_id, name, birth_date):
        super().__init__(animal_id, name, "Camel", birth_date, ["Walk", "Carry Load"])

class Donkey(PackAnimals):
    def __init__(self, animal_id, name, birth_date):
        super().__init__(animal_id, name, "Donkey", birth_date, ["Walk", "Carry Load", "Bray"])
