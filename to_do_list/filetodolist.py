from todolist import TodoList, Todo
import json
import os

class FileTodoList(TodoList):
    def __init__(self, filename: str):
        """
        Initializes a new instance of the `FileTodoList` class.

        Args:
            filename (str): The name of the file to load the todo list from.

        Returns:
            None
        """
        super().__init__()
        self.filename = filename
        self.load()

    def load(self) -> None:
        """
        Loads todo list data from a JSON file based on the specified filename.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for todo_data in data:
                    todo = Todo(todo_data['title'], todo_data['description'])
                    todo.id = todo_data['id']
                    todo.done = todo_data['done']
                    self.todos.append(todo)

    def save(self) -> None:
        """
        Saves the current list of todos to a file in JSON format.

        Returns:
            None
        """
        data = []
        for todo in self.todos:
            data.append({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'done': todo.done
            })
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def add_todo(self, title: str, description: str) -> None:
        """
        Adds a new todo item to the list of todos and saves the list.

        Args:
            title (str): The title of the todo item.
            description (str): The description of the todo item.

        Returns:
            None
        """
        super().add_todo(title, description)
        self.save()

    def delete_todo(self, todo_index: int) -> None:
        """
        Deletes a todo item from the list of todos and saves the updated list.

        Args:
            todo_index (int): The index of the todo item to delete.

        Returns:
            None
        """
        super().delete_todo(todo_index)
        self.save()

    def mark_as_done(self, todo_index: int) -> None:
        """
        Marks a todo item as done at the specified index and saves the updated list.

        Args todo_index: An integer representing the index of the todo item to mark as done.

        Returns:
            None
        """
        super().mark_as_done(todo_index)
        self.save()

    def update_todo(self, todo_index: int) -> None:
        """
        Updates a todo item in the todo list based on the provided index.
        This method calls the update_todo method of the parent class and then saves the updated list.

        Args:
            todo_index (int): The index of the todo item to update.

        Returns:
            None

        """
        super().update_todo(todo_index)
        self.save()