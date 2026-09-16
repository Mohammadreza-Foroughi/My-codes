from random import randint 

person_1 = []
person_2 = []

def roll_the_dice():
    random_number = randint(1,6)
    return random_number

def first_person():
    total = 0
    print("Player 1's turn: ")
    while True:
        user_input = input('Roll (r) or Hold(h) ? ').lower()
        if user_input == 'r':
            roll = roll_the_dice()
            if roll == 1:
                total == 0
                print(f'Your number is {roll}\nBust!')
                break
            total += roll
            print(f'Your number is {roll}\nYour total score is {total}')
        
        elif user_input == 'h':
            person_1.append(total)
            print(f'your score is {sum(person_1)}')
            break

        else:
            print('enter a valid value')

def second_person():
    total = 0
    print("Player 2's turn: ")
    while True:
        user_input = input('Roll (r) or Hold(h) ? ').lower()
        if user_input == 'r':
            roll = roll_the_dice()
            if roll == 1:
                total == 0
                print(f'Your number is {roll}\nBust!')
                break
            total += roll
            print(f'Your number is {roll}\nYour total score is {total}')
        
        elif user_input == 'h':
            person_2.append(total)
            print(f'your score is {sum(person_2)}')
            break

        else:
            print('enter a valid value')



def main():
    while True:
        first_person()
        if sum(person_1) >= 30:
            print('Player 1 is the winner !!!')
            break
        
        second_person()
        if sum(person_2) >= 30:
            print('Player 2 is the winner !!!')
            break

        
        



if __name__ == '__main__':
    main()