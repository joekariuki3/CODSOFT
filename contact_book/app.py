#!/usr/bin/env python
"""contact book app
"""

from contact_book_model import ContactBook

def add_new_contact():
    """
    Adds a new contact to the contact book.

    This function prompts the user to enter the contact's name, phone number, email, and address.
    It then creates a new `ContactBook` instance and adds the contact to it.
    Finally, it prints a message indicating that the contact has been added, along with the contact's name and phone number.

    Parameters:
        None

    Returns:
        None
    """
    name = input('Enter the contact name: ')
    phone = input('Enter the contact phone number: ')
    email = input('Enter the contact email: ')
    address = input('Enter the contact address: ')
    contact = ContactBook()
    new_contact = contact.add_contact(name=name, phone=phone, email=email, address=address)
    print(f'New contact added: ({new_contact.name}: {new_contact.phone})')

def terminate() -> None:
    """
    Terminate message for the program.
    """
    print('Goodbye!')

options = {
    1: ('New Contact', lambda: add_new_contact()),
    2: ('Edit Contact', lambda: print('Editing a contact is not supported yet. coming soon')),
    3: ('View Contact', lambda: print('Viewing a contact is not supported yet. coming soon')),
    4: ('Delete Contact', lambda: print('Deleting a contact is not supported yet. coming soon')),
    5: ('Exit', lambda: terminate()),
}
def main():
    """
    A function that runs the Contact book app, displaying options, taking user input,
    and executing the selected option until the user decides to exit.
    It handles user input validation and option execution, providing feedback on invalid inputs.
    """
    print('Contact book app')
    running = True
    while running:
        for option in options:
            print(f'[{option}] {options[option][0]}', end=' | ')
        try:
            option = int(input('\nEnter an option: '))
            if option < 1 or option > len(options):
                raise ValueError
            options[option][1]()
            if option == 5:
                running = False
        except:
            print('Invalid option. Exiting.')
if __name__ == '__main__':
    main()