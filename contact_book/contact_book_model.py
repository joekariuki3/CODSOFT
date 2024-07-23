import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from typing import Union

load_dotenv()

Base = declarative_base()

class contactModel(Base):
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

class ContactBook:
    def __init__(self)->None:
        """
        Initializes the class instance by setting up the database engine, creating all tables, and setting up a session for database interactions.

        Returns:
            None
        """
        self.engine = sqlalchemy.create_engine(os.getenv('DATABASE_URL'))
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def add_contact(self, name:str, phone:str, email:Union[str,None] = None, address: Union[str, None] = None) -> int:
        """
        Adds a new contact to the database.

        Args:
            name (str): The name of the contact.
            phone (str): The phone number of the contact.
            email (Union[str, None], optional): The email address of the contact. Defaults to None.
            address (Union[str, None], optional): The address of the contact. Defaults to None.

        Returns:
            contactModel: contact object.

        This function creates a new `contactModel` instance with the given `name`, `email`, `phone`, and `address`,
        and then adds it to the session and commits the changes to the database. Finally, it returns the ID of the
        newly added contact.
        """
        contact = contactModel(name=name, email=email, phone=phone, address=address)
        self.session.add(contact)
        self.session.commit()
        return contact