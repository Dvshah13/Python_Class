"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

enemy_skip = False
swap_switch = False

class Character(object):
   def __init__(self):
       self.name = '<undefined>'
       self.health = 10
       self.power = 5
       self.coins = 20

   def alive(self):
       return self.health > 0

   def attack(self, enemy):
       global swap_switch
       if not self.alive():
           return
       if swap_switch:
           print "%s attacks %s" % (self.name, enemy.name)
           enemy.receive_damage(enemy.power)
           time.sleep(1.5)
       else:
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
       self.health = 100
       self.power = 20
       self.coins = 20
       self.backpack = []
       self.armor = 10
       self.evade = 0
       self.evadescore = 0

   def restore(self):
       self.health = 10
       print "Hero's heath is restored to %d!" % self.health
       time.sleep(1)

   def buy(self, item):
       self.coins -= item.cost
       choice = 0
       print "To use now press 1\nTo store in your backpack press 2"
       while not(choice==1 or choice==2):
           choice = int(raw_input("What do you want to do with your item? "))
       if choice == 1:
           item.apply(hero)
       else:
           item.put_away(hero)

   def attack(self, enemy):
       if not self.alive():
           return
       if random.randint(1,6) == 1:
           super(Hero,self).attack(enemy)
           super(Hero,self).attack(enemy)
       else:
           super(Hero,self).attack(enemy)

   def receive_damage(self, points):
       if self.armor > 0 and self.armor >= points:
           points = 0
       else:
           points = points - self.armor
       if random.randint(1,101) < self.evadescore:
           pass
       else:
           self.health -= points
       print "%s received %d damage." % (self.name, points)
       print "These are your hit points: " + str(points)
       if self.health <= 0:
           print "%s is dead." % self.name

   def armorattack(self):
       if self.armor > 0:
           self.armor -= 2
           print "%s has %d armor" % (self.name, self.armor)
       else:
           self.armor = 0
           print "%s has %d armor" % (self.name, self.armor)


class Goblin(Character):
   def __init__(self):
       self.name = 'goblin'
       self.health = 6
       self.power = 2
class Medic(Character):
   def __init__(self):
       self.name = "medic"

   def restore(self):
       if random.randint(1,6) == 1 and self.health < 9:
           self.health +=2
           print "Medic regained 2 health. Medic's health is %d" % self.health
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
class Druid(Character):
   def __init__(self):
       self.name = 'druid'
       self.health = 8
       self.power = 3

   def shield(self):
       shield_strength = random.randint(1,3)
       return shield_strength

   def receive_damage(self, points):
       magic_shield = self.shield()
       if points < magic_shield:
           print "%s was shielded from all damage." % self.name
       else:
           super(Druid, self).receive_damage(points-magic_shield)
           print"%d damage was prevented with a magic shield!" % magic_shield
class Shadow(Character):
   def __init__(self):
       self.name = 'shadow'
       self.health = 1
       self.power = 1

   def generate_random(self):
       return random.randint(1,11)

   def receive_damage(self, points):
       if self.generate_random() == 1:
           super(Shadow, self).receive_damage(points)
       else:
           print "%s dissapeared before he could be hit" % self.name
class Berzerker(Character):
   def __init__(self):
       self.name = 'berzerker'
       self.health = 20
       self.power = 4

   def attack(self, enemy):
       if hero.alive():
           print "Berzerker is ENRAGED!\n"
           super(Berzerker, self).attack(enemy)
       for enemy in berzerker_enemies:
           if hero.alive() and self.alive():
               print "Berzerker is ENRAGED!\n"
               super(Berzerker, self).attack(enemy)
               if random.randint(1,3) == 1:
                   super(Berzerker, self).receive_damage(enemy.power)
           elif hero.alive() == False:
               print "Berzerker's Rage has been Sated by your death!"
               break
           elif self.alive() == False:
               break
class Zombie(Character):
   def __init__(self):
       self.name = 'zombie'
       self.power = 1

   def receive_damage(self, points):
       super(Zombie, self).receive_damage(points)
       print "%s was already dead. He gets back up" % self.name

class Battle(object):
   global enemy_skip
   enemy_skip = False
   def present_choices(self):
       print "-----------------------"
       print "What do you want to do?"
       print "1. fight %s" % enemy.name
       print "2. do nothing"
       print "3. flee"
       print "4. Open your backpack"
       print "> ",
       return int(raw_input())

   def run_inventory(self, enemy):
       while len(hero.backpack):
           for i in xrange(len(hero.backpack)):
               item = hero.backpack[i]
               print "%d.   %s" % (i + 1, item.name)
           input = int(raw_input("Enter an item number to use it or 0 to close backpack "))
           while input > len(hero.backpack) or input < 0:
               input = int(raw_input("Enter an item number to use it "))
           if input == 0:
               print "Back to the battle!"
               input = self.present_choices()
           else:
               if hero.backpack[i-1].name == 'swapspell':
                   hero.backpack[i-1].apply(hero, enemy)
               else:
                   hero.backpack[i-1].apply(hero)
               hero.backpack.pop(i-1)
       print "Backpack is empty"
       input = self.present_choices()
       while input >3 or input < 1:
           input = self.present_choices()
       return input

   def do_battle(self, hero, enemy):
       global swap_switch
       if enemy.alive():
           print "====================="
           print "Hero faces the %s" % enemy.name
           print "====================="
           while hero.alive() and enemy.alive():
               hero.print_status()
               enemy.print_status()
               time.sleep(1.5)
               input = self.present_choices()
               while input < 1 or input > 4:
                   input = self.present_choices()
               if input == 4:
                   input = self.run_inventory(enemy)
               if input == 1:
                   hero.attack(enemy)
               elif input == 2:
                   pass
               elif input == 3:
                   print "Goodbye."
                   exit(0)
               enemy.attack(hero)
               hero.armorattack()
               swap_switch = False
           if hero.alive():
               print "You defeated the %s" % enemy.name
               hero.bounty(enemy)
               return True
           else:
               print "YOU LOSE!"
               swap_switch = False
               return False
       else:
           return True
           enemy_skip = True
class Tonic(object):
   cost = 5
   name = 'tonic'
   def put_away(self,character):
       hero.backpack.append(self)

   def apply(self, character):
       character.health += 2
       print "%s's health increased to %d." % (character.name, character.health)

class SwapSpell(object):
   cost = 5
   name = 'swapspell'
   def put_away(self,character):
       hero.backpack.append(self)

   def apply(self, character, oponent):
       global swap_switch
       print "%s's health is now %d." % (character.name, oponent.health)
       print "%s's health is now %d." % (oponent.name, character.health)
       swap_switch = True
       return (character.health, oponent.health)
class Sword(object):
   cost = 10
   name = 'sword'
   def put_away(self,character):
       print 'A sword is meant to be swung!'
       self.apply(hero)
   def apply(self, hero):
       hero.power += 2
       print "%s's power increased to %d." % (hero.name, hero.power)
class Supertonic(Tonic):
   cost = 10
   name = 'super tonic'
   def put_away(self,character):
       hero.backpack.append(self)
   def apply(self, character):
       super(Supertonic, self).apply(character)
       super(Supertonic, self).apply(character)
       super(Supertonic, self).apply(character)
       super(Supertonic, self).apply(character)
       super(Supertonic, self).apply(character)
class Armor(object):
   cost = 5
   name = 'armor'
   def put_away(self,character):
       print 'Let\'s not walk around naked...'
       print 'Armor Applied'
       self.apply(hero)
   def apply(self, hero):
       hero.armor += 2
       print "%s's armor increased to %d." % (hero.name, hero.armor)
class Evade(object):
   cost = 2
   name = 'evade'
   def put_away(self,character):
       sure_check = raw_input("If you don't apply your Evasion Points, your chances to be hit won't go down. Are you sure you want to store this? Press 1 to Store or 2 to Apply" )
       if sure_check == 1:
           hero.backpack.append(self)
       else:
           self.apply(hero)
   def apply(self, hero):
       hero.evade += 2
       print "%s's evade increased to %d." % (hero.name, hero.evade)
       if hero.evade > 0:
           hero.evadescore = 10 + ((hero.evade-2) * 2.5)
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
   items = [Tonic, Sword, Supertonic, Armor, Evade, SwapSpell]
   def do_shopping(self, hero):
       global items
       while True:
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
               if hero.coins >= item.cost:
                   if item.name == 'sword':
                       hero.buy(item)
                       Store.items.pop(1)
                   else:
                       hero.buy(item)
               else:
                   print "You don't have enough coins"

hero = Hero()
berzerker_enemies = [Shadow(),Goblin(), Wizard(), Druid()]
enemies = [Berzerker()] + berzerker_enemies
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
   hero_won = battle_engine.do_battle(hero, enemy)
   if not hero_won:
       print "YOU LOSE!"
       exit(0)
   if enemy_skip == False:
       shopping_engine.do_shopping(hero)

print "YOU WIN!"
