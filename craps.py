from random import randrange

def dice_roll():
    pause = input("Press <enter> to roll the dice")
    roll = random.randrange(6)+1 + random.randrange(6)+1
    return roll
    print "You rolled a", roll

def main():
    response = raw_input("Do you want to play craps (Y or N)? ")
    response = response.upper()
    while response == 'Y':
        pause = input("Press <enter> to roll the dice")
        newroll = dice_roll()
        firstroll = dice_roll()
        if firstroll == 7 or firstroll == 11:
            print "You Won!"
        elif firstroll == 2 or firstroll == 3 or firstroll == 12:
            print "You Lost"
        else:
            print "We're going to try to roll the point!"
            point = firstroll
            newroll = random.randrange(6)+1 + random.randrange(6)+1

            newroll = dice_roll()
            while newroll != point and newroll != 7:
                newroll = random.randrange(6)+1 + random.randrange(6)+1
                newroll = dice_roll()
            if newroll == point:
                print "You Won!"
            else:
                print "You Lost!"

        response = raw_input("Do you want to play craps again (Y or N)? ")
    print "Good Bye!"

if _name_ == "_main_"
    main()
