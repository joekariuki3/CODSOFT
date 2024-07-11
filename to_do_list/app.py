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

    def add_todo(self, title: str, description: str) -> None:
        """
        Adds a new todo item to the list of todos.

        Args:
            title (str): The title of the todo item.
            description (str): The description of the todo item.

        Returns:
            None
        """
        todo = Todo(title, description)
        self.todos.append(todo)
        print(f'Todo item {todo.id} saved successfully!')

    def mark_as_done(self, todo_index: int) -> None:
        """
        A function that marks a todo item as done in the todo list.

        Parameters:
            todo_index (int): The index of the todo item to mark as done.

        Returns:
            None
        """
        try:
            todo = self.todos[todo_index]
            todo.completed()
            print(f'Todo "{todo.title}" marked as done successfully!')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

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

    def update_todo(self, todo_index: int) -> None:
        """
        A function that updates a todo item in the todo list based on the provided index.

        Args:
            todo_index (int): The index of the todo item to update.

        Returns:
            None
        """
        if len(self.todos) == 0:
            print('No todos to update. Please add a todo first!')
            return
        try:
            todo_index = int(todo_index)
            todo = self.todos[todo_index]
            print(f'Current todo: title: {todo.title}  description: {todo.description}')

            update_title = input('Update title ? (y/n): ')
            if update_title.lower() == 'y':
                new_title = input(f'Enter new title for "{todo.title}": ')
            else:
                new_title = todo.title
            update_description = input('Update description ? (y/n): ')
            if update_description.lower() == 'y':
                new_description = input(f'Enter new description for "{todo.title} Current description is {todo.description}": ')
            else:
                new_description = todo.description
            if update_description.lower() != 'y' and update_title.lower() != 'y':
                print('Update cancelled.')
                return
            # confirm update
            if self.confirm(f'Confirm update of "{todo.title}" to title "{new_title}" and description "{new_description}"?'):
                todo.title = new_title
                todo.description = new_description
                print(f'Todo "{todo.title}" updated successfully!')
            else:
                print('Update cancelled.')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

    def delete_todo(self, todo_index: int) -> None:
        """
        Deletes a todo item from the list of todos based on the provided index.

        Args:
            todo_index (int): The index of the todo item to delete.

        Returns:
            None

        Raises:
            IndexError: If the provided todo index is out of range.
            ValueError: If the provided todo index is not an integer.

        Prints:
            - If there are no todos in the todo list, prints a message indicating that there are no todos to delete.
            - If the provided todo index is valid, prints a message indicating that the todo item has been deleted successfully.
            - If the provided todo index is invalid, prints an error message indicating that the todo index is invalid.
            - If the deletion is cancelled by the user, prints a message indicating that the deletion has been cancelled.
        """
        if len(self.todos) == 0:
            print('No todos to delete. Please add a todo first!')
            return
        try:
            todo = self.todos[todo_index]
            # confirm deletion
            if self.confirm(f'Confirm deletion of "{todo.title}"?'):
                self.todos.pop(todo_index)
                print(f'Todo "{todo.title}" deleted successfully!')
            else:
                print('Deletion cancelled.')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

    def view_todo(self, todo_index: int) -> None:
        """
        A function that views the details of a todo item based on the provided index.

        Parameters:
            - todo_index (int): The index of the todo item to view.

        Returns:
            None
        """
        if len(self.todos) == 0:
            print('No todos to view. Please add a todo first!')
            return
        try:
            todo = self.todos[todo_index]
            print(f'Todo Index: {todo_index}')
            print(f'ID: {todo.id}')
            print(f'Title: {todo.title}')
            print(f'Description: {todo.description}')
            print(f'Status: {"Done" if todo.done else "Not done"}')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

    def view_completed_todos(self) -> None:
        """
        View the completed todos in the todo list.

        This function retrieves the completed todos from the `todos` list and prints their index, title, and description.
        If there are no completed todos, a message indicating that there are no completed todos to view is printed.

        Parameters:
            self (TodoList): The instance of the `TodoList` class.

        Returns:
            None
        """
        completed_todos = [todo for todo in self.todos if todo.done]
        if not completed_todos:
            print('No completed todos to view.')
            return
        for index, todo in enumerate(completed_todos, start=1):
            print(f'{index}: {todo.title} {todo.description} ({"Done" if todo.done else "Not done"})')

    def view_uncompleted_todos(self) -> None:
        """
        View the uncompleted todos in the todo list.

        This function retrieves the uncompleted todos from the `todos` list and prints their index, title, and description.
        If there are no uncompleted todos, a message indicating that there are no uncompleted todos to view is printed.

        Parameters:
            self (TodoList): The instance of the `TodoList` class.

        Returns:
            None
        """
        uncompleted_todos = [todo for todo in self.todos if not todo.done]
        if not uncompleted_todos:
            print('No uncompleted todos to view.')
            return
        for index, todo in enumerate(uncompleted_todos, start=1):
            print(f'{index}: {todo.title} {todo.description} ({"Done" if todo.done else "Not done"})')

    @staticmethod
    def confirm(prompt: str) -> bool:
        """
        Prompts the user to confirm an action.

        Parameters:
            prompt (str): The prompt to display to the user.

        Returns:
            bool: True if the user confirms, False otherwise.
        """
        while True:
            response = input(prompt +'(y/n): ')
            if response.lower() == 'y':
                return True
            elif response.lower() == 'n':
                return False
            else:
                print('Invalid response. Please enter y or n.')

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