from random import randint

def game():
    global correct_answer
    if correct_answer == False:
        name = raw_input("What is your name?: ")
        print "Hello %s!" % name
        ask = raw_input('Would you like to play a game of Craps? Type "yes" or "no": ')
        if ask == 'no':
            print "OK, maybe next time."
            correct_answer = True
        elif ask == 'yes':
            roll_dice()
            correct_answer = True
        else:
            print "Oops! Wrong answer. Let's try it again."
            correct_answer = False
            game()
    else:
        game()

def roll_dice():
    dice_roll = raw_input("Hit ENTER to roll the dice...")
    dice1 = randint(1,6)
    print dice1
    dice2 = randint(1,6)
    print dice2
    dice = dice1 + dice2
    print "You Rolled a total of %s" % dice

    if dice == 7 or dice == 11:
        print "Congratulations You Won!"
        ask = raw_input('Would you like to play again? Type "yes" or "no": ')
        if ask == "no":
            print "OK, maybe next time."
        elif ask == "yes":
            roll_dice()

    elif dice == 2 or dice == 3 or dice == 12:
        print "Better Luck Next Time."
        ask = raw_input('Would you like to play again? Type "yes" or "no": ')
        if ask == 'no':
            print "OK, maybe next time."
        elif ask == 'yes':
            roll_dice()

    else:
        print "You Get to Roll Again!"
        dice_roll
        reroll(dice)

def reroll(roll):
    dice_roll = raw_input("Hit ENTER to roll the dice...")
    dice1 = randint(1,6)
    print dice1
    dice2 = randint(1,6)
    print dice2
    dice = dice1 + dice2
    print "You Rolled a total of %s" % dice

    if dice == roll:
        print "Congratulations You Won!"
        ask = raw_input('Would you like to play again? Type "yes" or "no": ')
        if ask == 'no':
            print "OK, maybe next time."
        elif ask == 'yes':
            roll_dice()

    elif dice == 7 or dice == 11:
        print "Better Luck Next Time."
        ask = raw_input('Would you like to play again? Type "yes" or "no": ')
        if ask == 'no':
            print "OK, maybe next time."
        elif ask == 'yes':
            roll_dice()

    else:
        print "You Get to Roll Again!"
        dice_roll
        reroll(dice)

correct_answer = False
game()
