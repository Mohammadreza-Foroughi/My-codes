list_tasks = []

def input_check(user_input):
    try:
      if int(user_input) in range (1,4):
            return user_input
    except ValueError:
        print('Enter a valid choice!!!')

def Veiw_Task(1):
    print(list_tasks)

    
def main():
    while True:

        user_input = input('Todo List Menu:\n' \
        '1. Veiw Tasks\n' \
        '2. Add a Task\n' \
        '3. Remove a Task\n' \
        '4. Exit\n'
        'Enter your choice:')
        input_check(user_input) 
        Veiw_Task(1)
    

if __name__ == '__main__':
    main()