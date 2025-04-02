import random

def get_computer_choice():
    # Randomly select rock, paper, or scissors
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    # Ask the user for their choice and ensure it is valid
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    # Determine the winner of the game
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Get the user's and computer's choice
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Print both choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and print the result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
