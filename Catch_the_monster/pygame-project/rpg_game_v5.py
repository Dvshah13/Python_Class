"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
from random import randint


class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10

        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

    def bounty(self, enemy):
        self.coins += random.randint(5,8)
        print "%s has %d coins" % (self.name, self.coins)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 10
        self.evade = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def doubleattack(self, enemy):
        if random.randint(1,5) == 3:
            super(Hero, self).attack(enemy)
            super(Hero, self).attack(enemy)
        else:
            super(Hero, self).attack(enemy)

    def receive_damage(self, points):
        if self.armor > 0 and self.armor >= points:
            points = 0
        else:
            points = points - self.armor
        if randint(1,101) < evadescore:
            pass
        else:
            self.health -= points
        print "%s received %d damage." % (self.name, points)
        print "These are your hit points: " + str(points)
        if self.health <= 0:
            print "%s is dead." % self.name

        self.evadescore()

    def armorattack(self):
        if self.armor > 0:
            self.armor -= 2
            print "%s has %d armor" % (self.name, self.armor)
        else:
            self.armor = 0
            print "%s has %d armor" % (self.name, self.armor)

    def evadescore(self):
        if self.evade > 0:
            evadescore = ((self.evade-2)*2.5)+10







class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__ (self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.coins = 20

    def receive_damage(self, points):
        if random.randint(1,5) == 4:
            self.health += 2
        else:
            super(Medic, self).receive_damage(points)

class Shadow(Character):
    def __init__ (self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
        self.coins = 20

    def receive_damage(self, points):
        if random.randint(1,10) == 2:
            super(Shadow, self).receive_damage(points)
        else:
            self.health = 1
            print "%s received %d damage." % (self.name, points)

class Zombie(Character):
    def __init__ (self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
        self.coins = 20

    def alive(self):
        if self.health < 0:
            super(Zombie, self).alive(self)

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.doubleattack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
            hero.armorattack()
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.bounty(enemy)
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Supertonic(Tonic):
    cost = 10
    name = 'super tonic'
    def apply(self, character):
        super(Supertonic, self).apply(character)
        super(Supertonic, self).apply(character)
        super(Supertonic, self).apply(character)
        super(Supertonic, self).apply(character)
        super(Supertonic, self).apply(character)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Armor(object):
    cost = 5
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "%s's armor increased to %d." % (hero.name, hero.armor)

class Evade(object):
    cost = 2
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        print "%s's evade increased to %d." % (hero.name, hero.evade)

class Lottery(object):
    cost = 10
    name = 'lottery: enter at your own risk'
    def apply(self, hero):
        if random.randint(1,4) == 3:
            hero.coins += 40
            print "%s, wow you struck it RICH!!" % (hero.name)
        else:
            hero.coins -= 10
            print "%s rotten luck, sorry you lose 10 more :-(" % (hero.name)

class SuperSword(object):
    cost = 20
    name ='supersword'
    def apply(self, hero):
        hero.power += 8
        print "%s be careful swinging that thing, it's mighty powerful" % (hero.name)


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Supertonic, Armor, Evade, Lottery, SuperSword]
    def do_shopping(self, hero):
        while hero.coins > 0:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Medic(), Shadow(), Zombie()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"