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
