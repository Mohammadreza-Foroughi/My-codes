from termcolor import colored
import random

counter = [0]

def first_question():
    question_1 = input('Question 1: What is the capital of France? \nA. Berlin\nB. Madrid\nC. Paris\nD. Rome\nYour answer: ').lower()
    if question_1 == 'a' :
        print(colored('Correct!','green'))
        counter [0] += 1
    else:
        print(colored('Wrong! The correct answer is A','red'))
    

def second_question():
    question_2 = input('Qusetion 2: Which planet is known as the red planet? \nA. Earth\nB. Mars\nC. Jupiter\nD. Saturn\nYour answer: ').lower()
    if question_2 == 'b' :
        print(colored('Correct!','green'))
        counter [0] += 1
    else:
        print(colored('Wrong! The correct answer is B','red'))
    

def third_question():
    question_3 = input('Qusetion 3: What is the largest ocean on Earth? \nA. Atlantic\nB. Indian\nC. Arctic\nD. Pacific\nYour answer: ').lower()
    if question_3 == 'd' :
        print(colored('Correct!','green'))
        counter [0] += 1
    else:
        print(colored('Wrong! The correct answer is D','red'))
    

functions = [first_question,second_question,third_question]
random.shuffle(functions)
for func in functions:
    func()
print(f'Quiz over! Your final score is {counter[0]} out of 3')

# def main():
    # first_question()
    # second_question()
    # third_question()

# main()