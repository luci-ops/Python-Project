import random

# class GuessingGame:
#     def __init__(self, lower_num, upper_num):
#         self.lower_num = lower_num
#         self.upper_num = upper_num

#     def guess(self):
#         secret_number = random.randint(self.lower_num, self.upper_num)
#         attempts = 0
#         guess = 0

#         print("Welcome to the Guessing Game!")
#         print(f"I'm thinking of a number between {self.lower_num} and {self.upper_num}. Can you guess it?")

#         while guess != secret_number:
#             try:
#                 guess = int(input("Your guess: "))
#                 attempts += 1
#             except ValueError:
#                 print("Please enter a valid number.")

#             if guess < secret_number:
#                 print("Too low! Try a higher number.")
#             elif guess > secret_number:
#                 print("Too high! Try a lower number.")
#             else:
#                 print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

#         print("Game over. Let's play again!")

# # Initialize the game
# game = GuessingGame(1, 100)
# game.guess()


print("Welcome to Gussing Game")
range_upto = int(input("Enter the range you to play: "))
random_num = random.randint(0,range_upto)
gusses = 0
while True:
    gusses += 1
    gusse = input(f"Make a gusse between 0 to {range_upto}: \n")
    try:
        if gusse.isdigit():
            gusse = int(gusse)
        else:
            print("Enter valid Number")
            continue
    except ValueError:
        print("valid no.1")

    if gusse == random_num:
        print("Got IT!")
        break
    elif gusse < random_num:
        print("Too low")
    elif gusse > random_num:
        print("Too high")


print(f"You got the Gusse right in {gusses} attemps!")
