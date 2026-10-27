hero1 = {
    "name": "John Doe",
    "attack": 70,
    "defense": 50,
    "hp": 98,
    "mp": 100,
    "speed": 85,
    "strength": 58,
    "agility": 90,
    "intelligence": 85
}

hero2 = {
    "name": "Tom Smith",
    "attack": 85,
    "defense": 70,
    "hp": 80,
    "mp": 100,
    "speed": 70,
    "strength": 58,
    "agility": 90,
    "intelligence": 85
}

def take_damage(hero, damage):
    hero["hp"] = max(hero["hp"] - damage, 0)

take_damage(hero1, 50)
print(hero1)