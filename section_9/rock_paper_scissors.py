from random import choice

actions = ["rock", "paper", "scissors"]
comp_choice = choice(actions)

print("Let's play Rock, Paper, Scissors!")
print("Ready? Okayyy, Rock...Paper...Scissors..")
print("SHOOT!")

ans = input()

if (ans == comp_choice):
    print(f"Ooh, it appears because both of us had {ans}, we're tied!")
elif (ans == "rock" and comp_choice == "scissors"):
    print(f"Hey, you won! You got {ans} and I got {comp_choice}")
elif (ans == "rock" and comp_choice == "paper"):
    print(f"Sorry, I won! I got {comp_choice} while you got {ans}. Sorry :/")
elif (ans == "paper" and comp_choice == "rock"):
    print(f"Hey, you won! You got {ans} and I got {comp_choice}")
elif (ans == "paper" and comp_choice == "scissors"):
    print(f"Sorry, I won! I got {comp_choice} while you got {ans}. Sorry :/")
elif (ans == "scissors" and comp_choice == "paper"):
    print(f"Hey, you won! You got {ans} and I got {comp_choice}")
elif (ans == "scissors" and comp_choice == "rock"):
    print(f"Sorry, I won! I got {comp_choice} while you got {ans}. Sorry :/")
