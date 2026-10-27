# Следният код трябва да се разшири като:
# - Трябва да се добави атака която да е на случаен принцип за всеки от играчите. Числата трябва да са между 1 и 20
# - Трябва да се добави лекуване на всеки четен рунд за играчите със случайна стойност между 1 и 20.
#
# Задачата трябва да бъде качена и споделена в Github

import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount = None):
        if amount is None:
            amount = random.randint(1, 20)
        self.health += amount

    def attack(self, target, strength = None):
        if strength is None:
            strength = random.randint(1, 20)
        target.take_damage(strength)

    def is_alive(self):
        return self.health > 0

john = Character('John', 100)
alex = Character('Alex', 100)

round_number = 1

while john.is_alive() and alex.is_alive():
    print('Round ' + str(round_number))

    john.attack(alex)

    if alex.is_alive():
        alex.attack(john)

    if round_number % 2 == 0:
        john.heal()
        alex.heal()

    round_number += 1


if john.is_alive():
    print('Winner is John')
elif alex.is_alive():
    print('Winner is Alex')
else:
    print("They both are dead")
