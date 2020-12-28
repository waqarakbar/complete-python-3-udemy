from classes.game import bcolors, Person

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 45},
         {'name': 'Thunder', 'cost': 11, 'dmg': 54},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 43}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_spell_damage(1))