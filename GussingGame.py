import random

class GuessingGame:
    def __init__(self, lower_num, upper_num):
        self.lower_num = lower_num
        self.upper_num = upper_num

    def guess(self):
        secret_number = random.randint(self.lower_num, self.upper_num)
        attempts = 0
        guess = 0

        print("Welcome to the Guessing Game!")
        print(f"I'm thinking of a number between {self.lower_num} and {self.upper_num}. Can you guess it?")

        while guess != secret_number:
            try:
                guess = int(input("Your guess: "))
                attempts += 1
            except ValueError:
                print("Please enter a valid number.")

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! I guessed the number {secret_number} in {attempts} attempts.")

        print("Game over. Let's play again!")

# Initialize the game
game = GuessingGame(1, 100)
game.guess()