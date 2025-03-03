import random

#print(computer)

#print(user)
while True:
    computer=random.choice(['rock','paper','scissor'])
    user=input("select one 'rock'/'paper'/'scissor': ")
    print("computer choice",computer)
    print("user choice", user)
    if user not in ['rock','paper','scissor']:
        print("Invalid operation")
        break
    elif computer==user:
        print("tie")

    elif ((computer == 'rock' and user == 'scissor') or 
        (computer == 'scissor' and user == 'paper') or 
        (computer == 'paper' and user == 'rock')):
        print("Computer won!")

    else:
        print("user won")

    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing! Goodbye. 😊")
        break  # Exit the loop