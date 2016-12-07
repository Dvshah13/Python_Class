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

    if value==2 or value==3 or value==12:
        houseWins=True
        playerWins=False
        roundOver=True
        print "Player crapped out, house wins"
    elif value==7 or value==11:
        houseWins=False
        playerWins=True
        roundOver=True
        print "Player rolled a 7 or 11, player wins"
    else:
        point = value # set the point to the rolled value
        pointOn = True # track that the point has been set
        print "The point is on and set to: " + str(point)

    if pointOn:
        if point == value:
            print "Player wins"
            roundOver = True
            houseWins = False
            playerWins = True

while not roundOver:
    roll()


    #
    # point = value # set the point to the rolled value
    # pointOn = True # track that the point has been set
    # print "The point is on and set to: " + str(point)

    #
    #
    # if pointOn:
    #     if point == value:
    #         print "Player wins"
    #         roundOver = True
    #         houseWins = False
    #         playerWins = True
    # elif:
    #     point = value
    #     pointOn = True
    #     print "The point is on and set to: " + str(point)
    #
    # elif:
    #     if point==value: #player has matched the point
    #         print "Player hit the point, player wins"
    #     elif value==7:
    #         print "Player rolled a 7, house wins"
    #
    # else:
    #     if value==2 or value==3 or value==12:
    #         houseWins=True
    #         playerWins=False
    #         roundOver=True
    #         print "Player crapped out, house wins"
    #     elif value==7 or value==11:
    #         houseWins=False
    #         playerWins=True
    #         roundOver=True
    #         print "Player rolled a 7 or 11, player wins"
    #     else:
    #         point = value # set the point to the rolled value
    #         pointOn = True # track that the point has been set
    #         print "The point is on and set to: " + str(point)

# while not roundOver:
#     roll()

# def gameplay():
#     if not pointOn :
#         point = value # set the point to the rolled value
#         pointOn = True # track that the point has been set
#         print "The point is on and set to: " + str(point)
#
#     if pointOn:
#         if point == value: # player matched the point
#             print "Player hit the point, player wins"
#         elif value == 7:
#             print "Player rolled a 7, house wins"
#     else:
#         if value==2 or value==3 or value==12:
#             houseWins=True
#             playerWins=False
#             roundOver=True
#             print "Player crapped out, house wins"
#         elif value==7 or value==11:
#             houseWins=False
#             playerWins=True
#             roundOver=True
#             print "Player rolled a 7 or 11, player wins"
#         else:
#             point = value # set the point to the rolled value
#             pointOn = True # track that the point has been set
#             print "The point is on and set to: " + str(point)
#
#
# while not roundOver:
#     roll()
#     roll()
#     roll()
