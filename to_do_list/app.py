#!/usr/bin/env python3
from todolist import TodoList
from filetodolist import FileTodoList
from dbtodolist import DbTodoList
from dotenv import load_dotenv
import os

load_dotenv()

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
    todo_list_option = os.getenv('TODO_LIST_OPTION')

    if todo_list_option == 'in_memory':
        todo_list = TodoList()
    elif todo_list_option == 'file':
        filename = os.getenv('TODO_LIST_FILE')
        if filename is None:
            filename = input('Enter a filename: ')
        todo_list = FileTodoList(filename)
    elif todo_list_option == 'database':
        todo_list = DbTodoList()
    else:
        print('Choose a todo list option:')
        print('  1. In-memory list')
        print('  2. File list')
        print('  3. Database list')
        option = input('Enter an option: ')

        if option == '1':
            todo_list = TodoList()
        elif option == '2':
            filename = input('Enter a filename: ')
            todo_list = FileTodoList(filename)
        elif option == '3':
            todo_list = DbTodoList()
        else:
            print('Invalid option. Exiting.')
            return
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
    print(f'Using {todo_list_option} list')
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