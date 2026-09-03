import random
while True:
    
    #if I put (answer_input) out of the while loop because my value is not going to change I will 
    #get the same answer again and again because the valuse did not changed therefore I must put 
    #the (answer_input) inside the while loop to get new answers by changing the given input

    answer_input = input("Roll the dice? (y/n): ").lower()

    if answer_input != 'y' and answer_input != 'n' :
        print("Invalid choice!")

    elif answer_input == 'y'  :
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
        
    elif answer_input == 'n':
        print("Thanks for playing!")
        break
