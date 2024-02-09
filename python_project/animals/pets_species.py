# виды домашних животных и их действия

from pets import Pets

class Dog(Pets):
    def __init__(self, animal_id, name, birth_date):
        super().__init__(animal_id, name, "Dog", birth_date, ["Sit", "Stay", "Fetch"])

class Cat(Pets):
    def __init__(self, animal_id, name, birth_date):
        super().__init__(animal_id, name, "Cat", birth_date, ["Sit", "Pounce"])

class Hamster(Pets):
    def __init__(self, animal_id, name, birth_date):
        super().__init__(animal_id, name, "Hamster", birth_date, ["Roll", "Hide"])

