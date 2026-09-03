import random 

valid_choices = {'r' : '🪨' , 'p' : '📜' , 's' : '✂️'}



while True:

    question = input('Do you want to play? (y/n)').lower()
    if question == 'y':
        try:
            pc_choice = random.choice(list(valid_choices.values()))
            user_input = valid_choices[input("Rock, paper, or scissers? (r/p/s): ").lower()]

            if  user_input == pc_choice :
                print(f"You choice {user_input}\nComputer choice {pc_choice}\nYou Won!")
            elif    user_input != pc_choice :
                print(f"You choice {user_input}\nComputer choice {pc_choice}\nYou Lost!")

        except:
            print("Invalid choice")

    elif question == 'n':
        print("Have a good time!")
        break
    else:
            print("Enter a valid choice!!!")