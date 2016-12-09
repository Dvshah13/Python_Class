from random import randint;

secret_number = randint(1,10)

guesses = 0
print("I am thinking of a number between 1 and 10")

while guesses < 9:
    print("What's the number?")
    num = int(raw_input())

    guesses = guesses + 1

    if (num > secret_number):
        print("%d is too high")

    elif (num < secret_number):
        print("%d is too low")

    elif (num == secret_number):
        print("Yes, you win")
        break
