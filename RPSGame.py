import random
user = 0
computer = 0
options = ['rock','paper','scissors']
while True:
    user_input = input('Type rock,paper,scissors or q to quit:\n').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print("Enter Valid Input")
        continue
    random_No = random.randint(0,2)
    computer_gusse = options[random_No] 
    print('Computer pick ',computer_gusse)
    if user_input == 'rock' and computer_gusse == 'paper':
        print('computer win')
        computer += 1
    elif user_input == 'paper' and computer_gusse == 'scissors':
        print('computer win')
        computer += 1
    elif user_input == 'scissors' and computer_gusse == 'rock':
        print('computer win')
        computer += 1
    elif user_input == computer_gusse:
        print('Tie')
    else:
        print('You Win')
        user += 1
    
print('You Win: ',user ,'Computer Win: ',computer)
print('Goodbye')
    
