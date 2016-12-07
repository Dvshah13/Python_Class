from random import randint
# include the "randint" function from python's "random" module
pointOn = False
# is the point set: True or False
point = 0
# the value of the point
roundOver = False
#is the round over

def roll():
    # roll() function
    # roll dice
    d1 = randint(1,6) # get random number between 1 and 6
    d2 = randint(1,6) # get random number between 1 and 6
    value = d1+d2 # what the player rolled

    print "Player rolls a: " + str(value) # must convert the int value to a string

    if value == 7 or value == 11:
        print "You win"
    elif value == 2 or value == 3 or value == 12:
        print "You lose"
    else:
        print "We're going to try to roll the point! Point is set to: " + str(value)
        value = point
        newroll = randint(1,6) + randint(1,6)
        print "You rolled a " + str(newroll)
        while newroll != point and newroll != 7:
            newroll = randint(1,6) + randint(1,6)
            if newroll == point:
                print "You Won!"
            elif newroll == 7:
                print "You Lost!"

response = raw_input("Do you want to play? (Y or N)")
if response == "Y":
    roll()
else:
    print "Good Bye"
