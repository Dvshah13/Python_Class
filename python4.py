from random import randint;

guesses = 0
print("I am thinking of a number between 1 and 10")

while guesses < 5:
    print("What's the number?")
    num = int(raw_input())
    guesses = guesses + 1
    secret_number = randint(1,10)

    if (num > secret_number):
        print("%d is too high")

    elif (num < secret_number):
        print("%d is too low")

    elif (num == secret_number):
        print("Yes, you win")
print("You ran out of guesses!")

print("Do you want to play again (Y or N)?")
answer = raw_input()
if (answer == "Y"):
    guesses = 0
else:
    print("Bye")
