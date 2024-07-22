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
    phone = Column(String, nullable=False)
    email = Column(String)
    address = Column(String)

    def __repr__(self):
        return f'Contact(id={self.id}, name={self.name}, email={self.email}, phone={self.phone}, address={self.address})'

class ContactBook:
    def __init__(self)->None:
        self.engine = sqlalchemy.create_engine(os.getenv('DATABASE_URL'))
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def add_contact(self, name:str, phone:str, email:Union[str,None] = None, address: Union[str, None] = None) -> int:
        contact = contactModel(name=name, email=email, phone=phone, address=address)
        self.session.add(contact)
        self.session.commit()
        return contact.id