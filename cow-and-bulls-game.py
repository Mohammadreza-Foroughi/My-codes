from random import sample

def number_gen():
    """Return 4 unique digits as strings, e.g. ['3','7','0','5']."""
    return [str(d) for d in sample(range(10), 4)]

def is_valid_digit_guess() -> list:
    """Keep asking until the user enters 4 unique digits."""
    while True:
        user_input = input("Guess the number: ")
        if (user_input.isdigit() and len(user_input) == 4 and len(set(user_input)) == 4) == True:
            print(f'Your number is {user_input}')
            return list(user_input)
        else:
            print('Enter a valid non repeated 4-digit number')
            

def number_game_check(value,gen):
    """Return (bulls, cows)."""
    bulls = 0
    cows  = 0
    for index , number in enumerate(value):
        if number == gen[index]:
            bulls += 1
        elif number in gen:
            cows += 1
    return bulls, cows


def main():
    gen = number_gen()
    print('I have created a 4-digit number with unique digits. Try to guess it!')
    
    while True:
        value = is_valid_digit_guess()
        bulls, cows = number_game_check(value,gen)
        print(f"Bulls: {bulls}, Cows: {cows}")
        if bulls == 4 :
            print(f'You won!\n'
                f'The number is {("".join(gen))}')
            break 

if __name__ == '__main__':
    main()