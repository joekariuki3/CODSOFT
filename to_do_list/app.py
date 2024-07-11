#!/usr/bin/env python3
from todolist import TodoList

def terminate() -> None:
    """
    Terminates the program.

    Parameters:
    None

    Returns:
    None
    """
    print('Goodbye!')
    exit()

def main() -> None:
    todo_list = TodoList()
    options = {
        1: ('Add New Todo', lambda: todo_list.add_todo(input('Enter a title: '), input('Enter a description: '))),
        2: ('View Single Todo', lambda: todo_list.view_todo(int(input('Enter the index of the todo to view: ')))),
        3: ('View All Todos', todo_list.all),
        4: ('View Completed Todos', todo_list.view_completed_todos),
        5: ('View Uncompleted Todos', todo_list.view_uncompleted_todos),
        6: ('Mark as Complete', lambda: todo_list.mark_as_done(int(input('Enter the index of the todo to mark as done: ')))),
        7: ('Update Todo', lambda: todo_list.update_todo(int(input('Enter the index of the todo to update: ')))),
        8: ('Delete Todo', lambda: todo_list.delete_todo(int(input('Enter the index of the todo to delete: ')))),
        9: ('Exit', lambda: terminate()),
    }

    print('Welcome to the To Do List App!')
    while True:
        for key, (option, _) in options.items():
            print(f'{option} ({key})', end=' | ')
        option = input('\nChoose an option: ')

        try:
            option = int(option)
            if option < 1 or option > len(options):
                raise ValueError
            options[option][1]()
        except ValueError:
            print('Invalid option. Please enter a number.')

if __name__ == '__main__':
    main()