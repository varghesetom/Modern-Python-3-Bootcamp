import random

random_number = random.randint(1,10)

print("Let's play a guessing game!")
print("Guess a number between 1 and 10")

guess = 0

while (guess != random_number):
    guess = int(input("What is your guess "))
    if (guess > random_number):
        print("Ooh, sorry too high")
    elif (guess < random_number):
        print("Nah, too low")
    answer = input("Do you want to play again (y/n) ")
    if (answer == "n"):
        print(f"The number was {random_number}")
        break

if (guess == random_number):
    print("Yay you won! ")
