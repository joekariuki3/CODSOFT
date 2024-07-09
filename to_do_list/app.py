#!/usr/bin/env python3

import uuid

class Todo:
    def __init__(self, title: str, description: str):
        """
        Initializes a new instance of the `Todo` class.

        Args:
            title (str): The title of the todo item.
            description (str): The description of the todo item.

        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.done = False

    def save(self) -> str:
        """
        Returns the unique identifier of the instance.

        :return: A string representing the unique identifier of the instance.
        """
        return self.id

    def completed(self) -> None:
        """
        Marks the todo item as completed.

        This function sets the `done` attribute of the `Todo` instance to `True`, indicating that the todo item has been completed.

        Parameters:
            self (Todo): The `Todo` instance on which the method is called.

        Returns:
            None: This function does not return anything.
        """
        self.done = True

    def __repr__(self) -> str:
        """
        Returns a string representation of the Todo instance with its title, description, and done status.
        """
        return f'Todo({self.title}, {self.description}, done={self.done})'

class TodoList:
    def __init__(self):
        """
        Initializes a new instance of the `TodoList` class.
        """
        self.todos = []

    def add_todo(self, todo: Todo) -> None:
        """
        Adds a todo item to the list of todos.

        Parameters:
            todo (Todo): The todo item to be added.

        Returns:
            None: This function does not return anything.
        """
        self.todos.append(todo)

    def all(self) -> None:
        """
        Print the index and title of each todo item in the todo list.

        This method iterates over the `self.todos` list and prints the index and title, description of each todo item.
        If the todo item is marked as done, it also prints the description in parentheses.
        """
        for index, todo in enumerate(self.todos):
            if todo.done:
                print(f'{index}: {todo.title} {todo.description} (done)')
            else:
                print(f'{index}: {todo.title} {todo.description}')

def add_new_todo(todo_list: TodoList) -> None:
    """
    Adds a new todo item to the todo list provided.

    Parameters:
        todo_list (TodoList): The list of todos to add the new item.

    Returns:
        None
    """
    title = input('Enter a title: ')
    description = input('Enter a description: ')
    todo = Todo(title, description)
    todo_list.add_todo(todo)
    print(f'Todo item {todo.id} saved successfully!')

def mark_as_done(todo_list: TodoList) -> None:
    """
    A function that marks a todo item as done in the todo list.

    Parameters:
        todo_list (TodoList): The list of todos in which the todo item will be marked as done.

    Returns:
        None: This function does not return anything.
    """
    todo_index = input('Enter the index of the todo to mark as done: ')
    try:
        todo_index = int(todo_index)
        todo = todo_list.todos[todo_index]
        todo.completed()
        print(f'Todo "{todo.title}" marked as done successfully!')
    except (IndexError, ValueError):
        print('Invalid todo index. Please try again.')


def main() -> None:
    """
    The main function of the program. It initializes a TodoList and a dictionary of options.
    The options dictionary maps numbers to a tuple of strings. Each tuple contains
    the name of the option and a lambda function to execute when the option is chosen.

    The function then prints a welcome message and enters a loop to continuously
    prompt the user for an option. The user is expected to enter a number corresponding
    to one of the options in the dictionary. If the user enters a valid number,
    the corresponding lambda function is executed. If the user enters an invalid
    number, an error message is printed.

    Parameters:
    None

    Returns:
    None
    """
    todo_list = TodoList()
    options = {
        1: ('Add New Todo', lambda: add_new_todo(todo_list)),
        2: ('View Single Todo', lambda: print('Coming soon!')),
        3: ('View All Todos', todo_list.all),
        4: ('View Completed Todos', lambda: print('Coming soon!')),
        5: ('View Incomplete Todos', lambda: print('Coming soon!')),
        6: ('Mark as Complete', lambda: mark_as_done(todo_list)),
        7: ('Exit', lambda: exit(0)),
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