from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from todolist import TodoList, Todo
import os

Base = declarative_base()

class TodoModel(Base):
    __tablename__ = 'todos'
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    done = Column(Integer, default=0)

    def completed(self) -> None:
        """
        A function that marks the todo item as completed by setting the 'done' attribute to 1.
        """
        self.done = 1

    def __repr__(self):
        """
        Returns a string representation of the TodoModel instance.

        :return: A string representing the TodoModel instance with its id, title, description, and done status.
        """
        return f'TodoModel(id={self.id}, title={self.title}, description={self.description}, done={self.done})'

class DbTodoList(TodoList):
    def __init__(self):
        """
        Initializes the class instance by setting up the database engine, creating all tables, and setting up a session for database interactions.
        """
        super().__init__ ()
        self.engine = create_engine(os.getenv('DATABASE_URL'))
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_todo(self, title: str, description: str) -> None:
        """
        Adds a new todo item to the database.

        Args:
            title (str): The title of the todo item.
            description (str): The description of the todo item.

        Returns:
            None

        This function creates a new `Todo` instance with the given `title` and `description`,
        and then creates a corresponding `TodoModel` instance with the same `id`, `title`, and `description`.
        The `TodoModel` instance is then added to the session and the changes are committed to the database.
        Finally, a success message is printed indicating that the todo item was saved successfully.
        """
        todo = Todo(title, description)
        todo_model = TodoModel(id=todo.id, title=title, description=description)
        self.session.add(todo_model)
        self.session.commit()
        print(f'Todo item {todo.id} saved successfully!')

    def mark_as_done(self, todo_index: int) -> None:
        """
        Marks a todo item as done based on the provided todo_indexs.

        Args:
            todo_index (int): The index of the todo item to mark as done.

        Returns:
            None
        """
        try:
            todo_model = self.session.query(TodoModel).filter_by(id=self.todos[todo_index].id).first()
            todo_model.completed()
            self.session.commit()
            print(f'Todo "{todo_model.title}" marked as done successfully!')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

    def all(self) -> None:
        """
        Retrieves all todo items from the database using the session and stores them in `self.todos`.
        Calls the parent class's `all` method.
        """
        self.todos = self.session.query(TodoModel).all()
        super().all()

    def update_todo(self, todo_index: int) -> None:
        """
        Updates a todo item in the todo list based on the provided index.

        Args:
            todo_index (int): The index of the todo item to update.

        Returns:
            None

        Raises:
            IndexError: If the todo_index is out of range.
            ValueError: If the todo_index is not an integer.

        This function queries the database to find the todo item with the given index and prompts the user to update the title and description. If the user confirms the update, the changes are committed to the database. If the update is cancelled or the todo_index is invalid, an appropriate message is printed.
        """
        try:
            todo_model = self.session.query(TodoModel).filter_by(id=self.todos[todo_index].id).first()
            print(f'Current todo: title: {todo_model.title}  description: {todo_model.description}')

            update_title = input('Update title? (y/n): ')
            if update_title.lower() == 'y':
                new_title = input(f'Enter new title for "{todo_model.title}": ')
            else:
                new_title = todo_model.title
            update_description = input('Update description? (y/n): ')
            if update_description.lower() == 'y':
                new_description = input(f'Enter new description for "{todo_model.title} Current description is {todo_model.description}": ')
            else:
                new_description = todo_model.description
            if update_description.lower()!= 'y' and update_title.lower()!= 'y':
                print('Update cancelled.')
                return
            # confirm update
            if self.confirm(f'Confirm update of "{todo_model.title}" to title "{new_title}" and description "{new_description}"?'):
                todo_model.title = new_title
                todo_model.description = new_description
                self.session.commit()
                print(f'Todo "{todo_model.title}" updated successfully!')
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
        try:
            todo_model = self.session.query(TodoModel).filter_by(id=self.todos[todo_index].id).first()
            # confirm deletion
            if self.confirm(f'Confirm deletion of "{todo_model.title}"?'):
                self.session.delete(todo_model)
                self.session.commit()
                print(f'Todo "{todo_model.title}" deleted successfully!')
            else:
                print('Deletion cancelled.')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

    def view_todo(self, todo_index: int) -> None:
        """
        Retrieves and displays the details of a specific todo item based on the provided todo_index.

        Args:
            todo_index (int): The index of the todo item to view.

        Returns:
            None
        """
        try:
            todo_model = self.session.query(TodoModel).filter_by(id=self.todos[todo_index].id).first()
            print(f'Todo Index: {todo_index}')
            print(f'ID: {todo_model.id}')
            print(f'Title: {todo_model.title}')
            print(f'Description: {todo_model.description}')
            print(f'Status: {"Done" if todo_model.done else "Not done"}')
        except (IndexError, ValueError):
            print('Invalid todo index. Please try again.')

    def view_completed_todos(self) -> None:
        """
        Views all completed todos in the database.

        This function retrieves all completed todo items from the database using a query to filter by the 'done' attribute set to 1. If no completed todos are found, it prints a message indicating that there are no completed todos to view. Otherwise, it iterates over the completed todos and prints their index, title, description, and done status.

        Parameters:
            None

        Returns:
            None
        """
        completed_todos = self.session.query(TodoModel).filter_by(done=1).all()
        if not completed_todos:
            print('No completed todos to view.')
            return
        for index, todo_model in enumerate(completed_todos, start=1):
            print(f'{index}: {todo_model.title} {todo_model.description} ({"Done" if todo_model.done else "Not done"})')

    def view_uncompleted_todos(self) -> None:
        """
        Views all uncompleted todos in the database.

        This function retrieves all uncompleted todo items from the database using a query to filter by the 'done' attribute set to 0. If no uncompleted todos are found, it prints a message indicating that there are no uncompleted todos to view. Otherwise, it iterates over the uncompleted todos and prints their index, title, description, and done status.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        uncompleted_todos = self.session.query(TodoModel).filter_by(done=0).all()
        if not uncompleted_todos:
            print('No uncompleted todos to view.')
            return
        for index, todo_model in enumerate(uncompleted_todos, start=1):
            print(f'{index}: {todo_model.title} {todo_model.description} ({"Done" if todo_model.done else "Not done"})')

    def close(self):
        """
        Closes the session in the database connection.

        This function closes the session associated with the database connection. It does not take any parameters and does not return any value.
        """
        self.session.close()