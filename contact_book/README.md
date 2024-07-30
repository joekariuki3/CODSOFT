# Contact Book Application

This is a Python-based Contact Book application that allows users to add, view, update, and delete contacts. The application includes both a command-line interface (CLI) and a graphical user interface (GUI) using CustomTkinter.

## Features

- Add new contacts with name, phone, email, and address.
- View all contacts, sorted alphabetically.
- Update contact details.
- Delete contacts.
- GUI with scrollable contact list.
- Display contact count.
- Refresh contacts list.

## **Run Locally**

clone the CODSOFT directory

```bash
git clone https://github.com/joekariuki3/CODSOFT.git
```

Navigate to the todo project directory:

```bash
cd contact-book
```

Rename `.env.example` file to `.env` then Edit the environment variables accordingly

Create python virtual environment with name venv

```bash
python -m venv venv
```

Activate the python virtual environment

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Give app.py execution permissions

```bash
sudo chmod u+x app.py
```

```
sudo chmod u+x guiapp.py
```

## Usage

### Command Line Interface (CLI)

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Follow the on-screen instructions to add, view, update, or delete contacts.**

### Graphical User Interface (GUI)

1. **Run the application:**

   ```bash
   python guiapp.py
   ```

2. **Use the GUI to manage your contacts.**

## File Structure

- `app.py`: CLI implementation of the Contact Book.
- `contact_book_model.py`: Defines the database model and operations.
- `guiapp.py`: GUI implementation of the Contact Book using CustomTkinter.
- `requirements.txt`: List of dependencies.

## Dependencies

- `customtkinter`: For GUI components.
- `sqlalchemy`: For ORM and database interaction.
- `python-dotenv`: For loading environment variables from a `.env` file.

## Contributing

Contributions are welcome! Please create a pull request with a clear description of the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the developers of CustomTkinter for providing an excellent library for building modern Tkinter GUIs.

---
