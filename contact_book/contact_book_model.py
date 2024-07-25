import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from typing import Union, List

load_dotenv()

Base = declarative_base()

class ContactModel(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String)
    address = Column(String)

    def __repr__(self):
        """
        Returns a string representation of the Contact object.

        :return: A string representation of the Contact object.
        """
        return f'Contact(id={self.id}, name={self.name}, email={self.email}, phone={self.phone}, address={self.address})'

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the Contact object.

        Returns:
            dict: A dictionary representation of the Contact object with its id, name, email, phone, and address.

        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

class ContactBook:
    def __init__(self)->None:
        """
        Initializes the class instance by setting up the database engine, creating all tables, and setting up a session for database interactions.

        Returns:
            None
        """
        self.engine = sqlalchemy.create_engine(os.getenv('DATABASE_URL'))
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)
        self.session = self.session()

    def add_contact(self, name: str, phone: str, email: Union[str, None] = None, address: Union[str, None] = None) -> ContactModel:
        """
        Adds a new contact to the database.

        Args:
            name (str): The name of the contact.
            phone (str): The phone number of the contact.
            email (Union[str, None], optional): The email address of the contact. Defaults to None.
            address (Union[str, None], optional): The address of the contact. Defaults to None.

        Returns:
            ContactModel: The newly created contact object.

        Raises:
            ValueError: If a contact with the same phone number already exists in the database.

        This function creates a new `ContactModel` object with the given name, email, phone, and address. It then adds the contact to the session and attempts to commit the changes to the database. If a `sqlalchemy.exc.IntegrityError` is raised, indicating a duplicate phone number, the session is rolled back and a `ValueError` is raised. Otherwise, the newly created contact object is returned.
        """
        contact = ContactModel(name=name, email=email, phone=phone, address=address)
        self.session.add(contact)
        try:
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()
            raise ValueError("A contact with this phone number already exists.")
        return contact

    def get_contact(self, contact_id: int) -> ContactModel:
        """
        Returns a contact from the database.

        Args:
            contact_id (int): The ID of the contact to retrieve.

        Returns:
            ContactModel: contact object.

        This function returns a `ContactModel` object in the session with the given `contact_id`.
        """
        return self.session.query(ContactModel).filter_by(id=contact_id).first()

    def get_all_contacts(self) -> List[ContactModel]:
        """
        Returns a list of all contacts in the database.

        Returns:
            list[ContactModel]: A list of all contacts in the database.

        This function returns a list of all `ContactModel` objects in the session.
        """
        return self.session.query(ContactModel).all()

    def update_contact(self, contact_id: int, name: str, email: Union[str, None] = None, phone: Union[str, None] = None, address: Union[str, None] = None) -> None:
        """
        Updates a contact in the database with the given contact ID.

        Args:
            contact_id (int): The ID of the contact to update.
            name (str): The new name of the contact.
            email (Union[str, None], optional): The new email address of the contact. Defaults to None.
            phone (Union[str, None], optional): The new phone number of the contact. Defaults to None.
            address (Union[str, None], optional): The new address of the contact. Defaults to None.

        Returns:
            None: This function does not return anything.

        Raises:
            None

        This function retrieves a contact from the database with the given contact ID. If the contact exists, it updates the contact's name, email, phone, and address with the provided values. It then commits the changes to the database.
        """
        contact = self.get_contact(contact_id)
        if contact:
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.address = address
            self.session.commit()

    def delete_contact(self, contact_id: int) -> None:
        """
        Deletes a contact from the database.

        Args:
            contact_id (int): The ID of the contact to delete.

        Returns:
            None

        This function deletes a `ContactModel` object in the session with the given `contact_id`. It then commits
        the changes to the database.
        """
        self.session.query(ContactModel).filter_by(id=contact_id).delete()
        self.session.commit()