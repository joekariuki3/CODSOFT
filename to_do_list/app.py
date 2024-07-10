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
        if len(self.todos) == 0:
            print('No todos to delete. Please add a todo first!')
            return
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


def update_todo(todo_list: TodoList) -> None:
    """
    Updates a todo item in the todo list provided based on user input for title and description.

    Parameters:
        todo_list (TodoList): The list of todos to update the item in.

    Returns:
        None
    """
    if len(todo_list.todos) == 0:
        print('No todos to update. Please add a todo first!')
        return
    todo_index = input('Enter the index of the todo to update: ')
    try:
        todo_index = int(todo_index)
        todo = todo_list.todos[todo_index]
        print(f'Current todo: title{todo.title}  description: {todo.description}')
        update_title = input('Update title ? (y/n): ')
        update_description = input('Update description ? (y/n): ')

        if update_title.lower() == 'y':
            new_title = input(f'Enter new title for "{todo.title}": ')
            todo.title = new_title
        if update_description.lower() == 'y':
            new_description = input(f'Enter new description for "{todo.title} Current description is {todo.description}": ')
            todo.description = new_description

        print(f'Todo "{todo.title}" updated successfully!')
    except (IndexError, ValueError):
        print('Invalid todo index. Please try again.')


def delete_todo(todo_list: TodoList) -> None:
    """
    Deletes a todo item from the todo list based on the index provided by the user.

    Parameters:
        todo_list (TodoList): The list of todos from which the todo item will be deleted.

    Returns:
        None: This function does not return anything.
    """
    if len(todo_list.todos) == 0:
        print('No todos to delete. Please add a todo first!')
        return

    todo_index = input('Enter the index of the todo to delete: ')
    try:
        todo_index = int(todo_index)
        todo = todo_list.todos.pop(todo_index)
        print(f'Todo "{todo.title}" deleted successfully!')
    except (IndexError, ValueError):
        print('Invalid todo index. Please try again.')

def view_todo(todo_list: TodoList) -> None:
    """
    View a specific todo item from the todo list based on the index provided by the user.

    Parameters:
        todo_list (TodoList): The list of todos from which the todo item will be viewed.

    Returns:
        None: This function does not return anything.

    Raises:
        IndexError: If the provided todo index is out of range.
        ValueError: If the provided todo index is not an integer.

    Prints:
        - If there are no todos in the todo list, prints a message indicating that there are no todos to view.
        - If the provided todo index is valid, prints the title, description, and status of the todo item.
        - If the provided todo index is invalid, prints an error message indicating that the todo index is invalid.
    """
    if len(todo_list.todos) == 0:
        print('No todos to view. Please add a todo first!')
        return

    todo_index = input('Enter the index of the todo to view: ')
    try:
        todo_index = int(todo_index)
        todo = todo_list.todos[todo_index]
        print(f'Todo Index: {todo_index}')
        print(f'ID: {todo.id}')
        print(f'Title: {todo.title}')
        print(f'Description: {todo.description}')
        print(f'Status: {"Done" if todo.done else "Not done"}')
    except (IndexError, ValueError):
        print('Invalid todo index. Please try again.')

def view_completed_todos(todo_list: TodoList) -> None:
    """
    View the completed todos in the given todo list.

    Args:
        todo_list (TodoList): The todo list to view completed todos from.

    Returns:
        None: This function does not return anything.

    Prints:
        - If there are no completed todos, prints a message indicating that there are no completed todos to view.
        - If there are completed todos, prints the index and title, description, and status of each completed todo item.
    """
    completed_todos = [todo for todo in todo_list.todos if todo.done]
    if not completed_todos:
        print('No completed todos to view.')
        return
    for index, todo in enumerate(completed_todos, start=1):
         print(f'{index}: {todo.title} {todo.description} ({"Done" if todo.done else "Not done"})')

def view_uncompleted_todos(todo_list: TodoList) -> None:
    """
    View the uncompleted todos in the given todo list.

    Args:
        todo_list (TodoList): The todo list to view uncompleted todos from.

    Returns:
        None: This function does not return anything.

    Prints:
        - If there are no uncompleted todos, prints a message indicating that there are no uncompleted todos to view.
        - If there are uncompleted todos, prints the index and title, description, and status of each uncompleted todo item.
    """
    uncompleted_todos = [todo for todo in todo_list.todos if not todo.done]
    if not uncompleted_todos:
        print('No uncompleted todos to view.')
        return
    for index, todo in enumerate(uncompleted_todos, start=1):
         print(f'{index}: {todo.title} {todo.description} ({"Done" if todo.done else "Not done"})')

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
        2: ('View Single Todo', lambda: view_todo(todo_list)),
        3: ('View All Todos', todo_list.all),
        4: ('View Completed Todos', lambda: view_completed_todos(todo_list)),
        5: ('View Uncompleted Todos', lambda: view_uncompleted_todos(todo_list)),
        6: ('Mark as Complete', lambda: mark_as_done(todo_list)),
        7: ('Update Todo', lambda: update_todo(todo_list)),
        8: ('Delete Todo', lambda: delete_todo(todo_list)),
        9: ('Exit', lambda: exit(0)),
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