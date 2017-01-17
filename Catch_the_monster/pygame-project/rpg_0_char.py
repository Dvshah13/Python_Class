"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def alive (self):
        if self.health > 0:
            return True

    def attack (self, char1):
        goblin.health -= self.power
        print "You do %d damage to the goblin." % self.power
        if goblin.health <= 0:
            print "The goblin is dead."

    def print_status (self):
        print "You have %d health and %d power." % (self.health, self.power)

class Hero(Character):
    def __init__ (self):
        self.health = 10
        self.power = 5
        Character.alive(self)
        Character.attack(self, Goblin)
        Character.print_status(self)


class Goblin(Character):
    def __init__ (self):
        self.health = 6
        self.power = 2
        Character.alive(self)
        Character.attack(self, Hero)

    def attack(self,hero):
        hero.health -= self.power
        print "The goblin does %d damage to you." % self.power
        if hero.health <= 0:
            print "You are dead."

    def print_status(self):
        print "The goblin has %d health and %d power." % (self.health, self.power)

def main():
    goblin = Goblin()
    hero = Hero()
    character = Character()

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            # goblin.health -= hero.power
            # print "You do %d damage to the goblin." % hero.power
            # if goblin.health <= 0:
            #     print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            # hero.health -= goblin.power
            # print "The goblin does %d damage to you." % goblin.power
            # if hero.health <= 0:
            #     print "You are dead."

main()
