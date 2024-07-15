# todo list application.

## Allows users to create, update and track their to-do lists. Developed in python

## **Features**

- Create new todo items with a title and description
- View all todo items in the list
- Mark todo items as completed
- Update todo items (title, description, or status)
- Delete todo items
- View completed and uncompleted todo items separately

## **Run Locally**

clone the CODSOFT directory

```bash
git clone https://github.com/joekariuki3/CODSOFT.git
```

Navigate to the todo project directory:

```bash
cd to_do_list
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

Run the application

```bash
./app.py
```
