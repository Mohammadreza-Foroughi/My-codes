from random import randint

pc_number = randint(1,100)

while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))

    
        if user_guess == pc_number :
            print(f"Congratulation! You guessed the number.\nThe number: {pc_number}")
            break
        elif user_guess > pc_number:
            print("Too High!")
        elif user_guess < pc_number:
            print("Too Low!")
    except:
            print("Please enter a valid number")