#!/usr/bin/env python3

import uuid

TO_DO_LIST = []

class Todo:
    def __init__(self, title, description):
        """
        Initializes a new instance of the `Todo` class.

        Args:
            title (str): The title of the todo item.
            description (str): The description of the todo item.
            done (bool): A flag indicating whether the todo item is done or not.

        Returns:
            None
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.done = False

    def save(self):
        todo_item = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done
        }
        TO_DO_LIST.append(todo_item)
        return self.id
    def completed(self):
        self.done = True

print('Welcome to the To Do List App!')
options = ['Add New Todo','view single Todo', 'View All Todos', 'View Completed Todos', 'View Incomplete Todos', 'Mark as Complete', 'Exit']
print('Options:', ', '.join(options))
print('Select an option:')
while True:
    title = input('Enter a title: ')
    description = input('Enter a description: ')
    todo = Todo(title, description)
    todo_id = todo.save()
    print(f'Todo item {todo_id} saved successfully!')