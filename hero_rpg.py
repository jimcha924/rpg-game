# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def Attack(self, enemy):
        enemy.health -= self.power
        print('{} dealt {} damage to {}!!' .format(self.name, self.power, enemy.name))

    def print_status(self):
        print('{} has {} health.' .format(self.name, self.health))

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

class Hero(Character): 
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # def Attack(self, enemy):
    #     enemy.power -= self.health
    #     print('You dealt {} damage to the goblin!!' .format(self.power))

    # def print_status(self):
    #     print('The hero has {} health.' .format(self.health))


class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Zombie(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # def Attack(self, enemy):
    #     enemy.power -= self.health
    #     print('You dealt {} damage to the goblin!!' .format(self.power))

    # def print_status(self):
    #     print('The goblin has {} health.' .format(self.health))


def main():
    hero = Character("Brave Sir Robin", 10, 0)
    # hero = Character("Brave Sir Robin", 10, 0)
    goblin = Character("The Black Knight", 6, 2)
    zombie = Character("Zero", 1000000000000000000, 5)

    while hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The zombie has infinite health and {} power.".format(zombie.power))
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. run away!!")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.Attack(zombie)
            if goblin.health <= 0:
                print("The goblin is dead, Jim.")
        elif raw_input == "2":
            zombie.Attack(hero)
        elif raw_input == "3":
            print("Brave Sir Robin ran away!")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.health > 0:
            if hero.health <= 0:
                print("Brave Sir Robin has died having his face eaten off.")
                # print("Our hero has died in the heat of battle.")

main()