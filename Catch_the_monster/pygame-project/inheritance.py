class Animal(object):
    def breed(self):
        return Animal()
    def makeNoise(self):
        print "I am an animal"

class Dog(Animal):
    def woof(self):
        print 'Woof'

class Cat(Animal):
    def meow(self):
        print 'Meow'
c = Cat()
d = Dog()
