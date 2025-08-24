def main():
    print("Welcome to Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()

def print_rules():
    print("""
Rules of Rock, Paper, Scissors:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both players choose the same, it’s a tie
""")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print_rules()

if __name__ == "__main__":
    main()

import random

def print_rules():
    print("""
Rules of Rock, Paper, Scissors:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both players choose the same, it’s a tie
""")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print_rules()

    choices = ["rock", "paper", "scissors"]
    player = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

if __name__ == "__main__":
    main()


import random

def print_rules():
    print("""
Rules of Rock, Paper, Scissors:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both players choose the same, it’s a tie
""")

def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print_rules()

    choices = ["rock", "paper", "scissors"]
    player = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")
    print(decide_winner(player, computer))

if __name__ == "__main__":
    main()



