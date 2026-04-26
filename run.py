import random

print("WELCOME TO THE GAME")

choices = ["stone", "paper", "scissors"]

while True:
    user = input("\nEnter Stone, Paper or Scissors (or type exit to quit): ").strip().lower()

    if user == "exit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid input! Please enter stone, paper, or scissors.")
        continue

    comp = random.choice(choices)

    print(f"You chose {user} and computer chose {comp}")

    # 🔹 Condition logic here
    if user == comp:
        print("It's a tie!")

    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        print("You WIN!")

    else:
        print("Computer WINS!")