import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choice = input("Enter your choice (1/2/3): ")
    choices = {"1": "rock", "2": "paper", "3": "scissors"}
    return choices.get(choice, None)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"


print("===== ROCK PAPER SCISSORS GAME =====")
print("Rules:")
print("- Rock beats Scissors")
print("- Scissors beats Paper")
print("- Paper beats Rock")

user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()

    if not user_choice:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = get_computer_choice()

    print(f"\nYour choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("Result: Ohh no,It's a tie!")
    elif result == "user":
        print("Result: yay,You win this round!")
        user_score += 1
    else:
        print("Result: Computer wins this round!")
        computer_score += 1

    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again != "y":
        print("\nThank you for playing!")
        break
