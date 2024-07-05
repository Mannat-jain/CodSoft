#rock-paper-scissor game
import random

def display_choice(choice):
    if choice == "rock":
        return '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
    elif choice == "paper":
        return '''
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        '''
    elif choice == "scissors":
        return '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''
    else:
        return "Invalid choice!"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
while user_choice not in choices:
    print("Invalid choice. Please try again.")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

computer_choice = random.choice(choices)
print(f"\nYou chose:{display_choice(user_choice)}")
print(f"Computer chose:{display_choice(computer_choice)}")

result = determine_winner(user_choice, computer_choice)
print(result)
