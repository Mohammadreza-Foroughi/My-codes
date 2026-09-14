list_tasks = []

def input_check(user_input):
    try:
        if int(user_input) in range (1,5):
            return user_input 
        else:
            print('Enter a valid choice!!!')
    except ValueError:
        print('Enter a valid choice!!!')

def veiw_task(accepted_input):
    if accepted_input == '1':
        for index, task in enumerate(list_tasks, 1):
            print(f'{index}. {task}')

def add_task(accepted_input):
    if accepted_input == '2':
        add_new = input('Enter a new task: ')
        list_tasks.append(add_new)
        
def remove_task(accepted_input):
    if accepted_input == '3':
        for index, task in enumerate(list_tasks, 1):
            print(f'{index}. {task}')
        try:
            delete_choice = int(input('Which task do you want to delete? '))
            list_tasks.pop(delete_choice - 1)
        except (ValueError, IndexError):
            print('Invalid choice.')

    
def main():
    while True:

        user_input = input('Todo List Menu:\n' \
        '1. Veiw Tasks\n' \
        '2. Add a Task\n' \
        '3. Remove a Task\n' \
        '4. Exit\n'
        'Enter your choice:')
        accepted_input = input_check(user_input) 
        if accepted_input == '4':
            print(list_tasks)
            break

        veiw_task(accepted_input)
        add_task(accepted_input)
        remove_task(accepted_input)
        print(list_tasks)

if __name__ == '__main__':
    main()