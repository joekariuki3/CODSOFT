#!/usr/bin/env python
"""contact book app
"""

from contact_book_model import ContactBook

def add_new_contact():
    """
    Adds a new contact to the contact book.

    This function prompts the user to enter the contact name, phone number, email, and address. It then creates a new `ContactBook` instance and adds the contact to the contact book using the `add_contact` method. If the contact is successfully added, it prints a message indicating the contact name and phone number. If there is an error, it prints the error message.

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
    try:
        new_contact = contact.add_contact(name=name, phone=phone, email=email, address=address)
        print(f'New contact added: ({new_contact.name}: {new_contact.phone})')
    except ValueError as e:
        print(e)

def view_contact():
    """
    Prints a contact in the contact book.

    This function creates a new `ContactBook` instance and prints a contact in the contact book.

    Parameters:
        None

    Returns:
        None
    """
    contact_id = int(input('Enter contact id: '))
    contact = ContactBook()
    current_contact = contact.get_contact(contact_id)
    if current_contact:
        print(f'Contact: {current_contact.to_dict()}')
    else:
        print('Contact not found')

def view_all_contacts():
    """
    Prints all contacts in the contact book.

    This function creates a new `ContactBook` instance and prints all the contacts in the contact book.

    Parameters:
        None

    Returns:
        None
    """
    contact = ContactBook()
    contacts = contact.get_all_contacts()
    for index, contact in enumerate(contacts):
        print(contact)

def edit_contact():
    """
    Edits a contact in the contact book.

    This function prompts the user to enter the contact id and allows them to edit the contact's name, phone number, email, and address. It creates a new `ContactBook` instance and retrieves the contact with the given id. If the contact exists, it prints the current contact details and prompts the user to enter the new values. The function then updates the contact with the new values and prints a success message along with the updated contact details. If the contact does not exist, it prints a message indicating that the contact was not found.

    Parameters:
        None

    Returns:
        None
    """
    contact_id = int(input('Enter contact id: '))
    contact = ContactBook()
    current_contact = contact.get_contact(contact_id)
    if current_contact:
        print(f'Current contact: {current_contact.to_dict()}')
        name = input(f'Enter new name ({current_contact.name}): ')
        phone = input(f'Enter new phone ({current_contact.phone}): ')
        email = input(f'Enter new email ({current_contact.email}): ')
        address = input(f'Enter new address ({current_contact.address}): ')
        if not name:
            name = current_contact.name
        if not phone:
            phone = current_contact.phone
        if not email:
            email = current_contact.email
        if not address:
            address = current_contact.address
        contact.update_contact(contact_id, name, email, phone, address)
        print('Contact updated successfully')
        print(f'Updated contact: {current_contact.to_dict()}')
    else:
        print('Contact not found')

def delete_contact():
    """
    Deletes a contact from the contact book.

    This function prompts the user to enter the contact ID of the contact to be deleted. It then creates a new `ContactBook` instance and calls the `delete_contact` method on it, passing in the contact ID. Finally, it prints a message indicating that the contact has been deleted successfully.

    Parameters:
        None

    Returns:
        None
    """
    contact_id = int(input('Enter contact id: '))
    contact = ContactBook()
    contact.delete_contact(contact_id)
    print('Contact deleted successfully')


def terminate() -> None:
    """
    Terminate message for the program.
    """
    print('Goodbye!')

options = {
    1: ('New Contact', lambda: add_new_contact()),
    2: ('Edit Contact', lambda: edit_contact()),
    3: ('View Contact', lambda: view_contact()),
    4: ('View Contacts', lambda: view_all_contacts()),
    5: ('Delete Contact', lambda: delete_contact()),
    6: ('Exit', lambda: terminate()),
}
def main():
    """
    A function that runs the Contact book app, displaying options, taking user input,
    and executing the selected option until the user decides to exit.
    It handles user input validation and option execution, providing feedback on invalid inputs.
    """
    print('Contact book app')
    running = True
    exit_option = len(options)
    while running:
        for option in options:
            print(f'[{option}] {options[option][0]}', end=' | ')
        try:
            option = int(input('\nEnter an option: '))
            if option < 1 or option > len(options):
                raise ValueError
            options[option][1]()
            if option == exit_option:
                running = False
        except Exception as error:
            print(f'Invalid option. Exiting.{error}')
if __name__ == '__main__':
    main()