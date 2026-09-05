import random 

valid_choices = {'r' : '🪨' , 'p' : '📜' , 's' : '✂️'}



while True:

    question = input('Do you want to play? (y/n)').lower()
    if question == 'y':
        try:
            pc_choice = random.choice(list(valid_choices.values()))
            user_input = input("Rock, paper, or scissers? (r/p/s): ").lower()
            print(f"Your choice {valid_choices[user_input]}\nComputer choice {pc_choice}")

            
            if  user_input == pc_choice :
                print("Tie!")
            elif ((user_input == 'r' and pc_choice == 's') or
                (user_input == 's' and pc_choice == 'p') or
                (user_input == 'p' and pc_choice == 'r') ):
                print("You Won!")
            else:
                print("You Lost!")


        except:
            print("Invalid choice")

    elif question == 'n':
        print("Have a good time!")
        break
    else:
            print("Enter a valid choice!!!")