# import time
# import random
#
# class Person(object):
#     alive = True
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def greet(self):
#         print "Hello " + self.longname()
#
#     def kill(self):
#         self.alive = False
#         print "We just killed " + self.fname
#
#     def longname(self):
#         return self.fname + " " + self.lname
#
# janice = Person("Janice", "Smith")
# janice.greet()
# bob = Person("Bob", "Jones")
# bob.greet()
#


# #basics
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
#
#     def print_contact_info(self,contact):
#         print "%s's email: %s, %s's phone number: %s" % (contact.name,contact.email,contact.name,contact.phone)
#
    # 1. sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
#     2. jordan = Person('Jordan','jordan@aol.com','495-586-3456')
#     3. sonny.greet(jordan)
#     4. jordan.greet(sonny)
#     5. print sonny.email, sonny.phone
#     6. print jordan.name, jordan.email, jordan.phone
#
# #make your own class and add a method

# class Vehicle(object):
#     def __init__(car, make, model, year):
#         car.make = make
#         car.model = model
#         car.year = year
#
#     def print_info(car):
#         print "%s %s %s" % (car.year, car.make, car.model)
# nissan = Vehicle("Nissan","Leaf","2015")
# nissan.print_info()

#add a method 2/add an instance variable
# class Person(object):
#     def __init__(self, name, email, phone, friends=[]):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = friends
#
#     def greet(self):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
#
#     def print_contact_info(self):
#         print "%s's email: %s, %s's phone number: %s" % (self.name,self.email,self.name,self.phone)
#
# sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# jordan = Person('Jordan','jordan@aol.com','495-586-3456')
# sonny.friends.append(jordan)
# jordan.friends.append(sonny)
#
# print len(sonny.friends)

#add a friends

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.greeting_count = 0

    def greet(self,other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1


    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.email, self.phone)


    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name,self.email,self.name,self.phone)

    def num_unique_people_greeted(self):
        self.unique_greeting += 1

    # def add_friend(self, friends):
    #     self.friends = friends
    #
    # def num_friends(self):
    #     print len(self.friends)



sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')


print sonny.num_unique_people_greeted()
sonny.greet(jordan)
