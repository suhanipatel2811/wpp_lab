import random

class Rock_paper_scissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds  # Total number of rounds in the game
        self.current_round = 0  # The current round number
        self.user_wins = 0  # Number of wins by the user
        self.computer_wins = 0  # Number of wins by the computer

    def get_computer_choice(self):
        # Randomly pick one of 'rock', 'paper', or 'scissors' for the computer
        return random.choice(['rock', 'paper', 'scissors'])

    def find_winner(self, user_choice, computer_choice):
        # Determine the winner of a round
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'user'
        else:
            return 'computer'

    def play_round(self, user_choice):
        if self.current_round >= self.total_rounds:
            return "Game over! All rounds have been played."

        # Get the computer's choice
        computer_choice = self.get_computer_choice()
        print(f"Round {self.current_round + 1}:")
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        # Determine the winner of the round
        winner = self.find_winner(user_choice, computer_choice)
        if winner == 'user':
            self.user_wins += 1
            print("You win this round!")
        elif winner == 'computer':
            self.computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        self.current_round += 1

    def is_game_over(self):
        # Check if the game has ended
        return self.current_round >= self.total_rounds

    def get_game_result(self):
        # Determine who won the overall game
        if self.user_wins > self.computer_wins:
            return f"You win the game with {self.user_wins} wins!"
        elif self.user_wins < self.computer_wins:
            return f"Computer wins the game with {self.computer_wins} wins!"
        else:
            return "The game is a tie!"

    def play_game(self):
        # Play the entire game by looping through the rounds
        while not self.is_game_over():
            user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
            while user_choice not in ['rock', 'paper', 'scissors']:
                user_choice = input("Invalid choice! Please enter 'rock', 'paper', or 'scissors': ").lower()
            
            self.play_round(user_choice)
        
        # At the end of all rounds, print the final result
        print(self.get_game_result())
# Create an instance of Rock_paper_scissors for 5 rounds
game = Rock_paper_scissors(total_rounds=5)

# Start the game
game.play_game()
