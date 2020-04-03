import random

number = random.randint(1,10)
guess = 0
while guess != number:
    print("Enter a number between 1 and 10")
    guess = int(input())
    if(guess>number):
        print("Guess lower")

    elif(guess<number):
        print("Guess higher")
print("You got it right!")