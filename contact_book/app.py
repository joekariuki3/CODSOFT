#!/usr/bin/env python
"""contact book app
"""

from contact_book_model import ContactBook

def main():
    print("Contact book app")
    contact_book = ContactBook()
    # test add contacts
    new_contact_id = contact_book.add_contact('John', '555-555-5555', 'nTl6w@example.com', '123 Main St')
    print(new_contact_id)

if __name__ == '__main__':
    main()