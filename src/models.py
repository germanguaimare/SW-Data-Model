import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(10), nullable=False, unique=True)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer,ForeignKey("User.id"),primary_key=True)
    charId = Column(String(120), ForeignKey("Characters.id"), nullable=True)
    vehicleID = Column(String(120), ForeignKey("Vehicles.id"), nullable=True)
    planetID = Column(String(120), ForeignKey("Planets.id"), nullable=True)


class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.

    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    charName = Column(String(120), nullable=False)
    charBirthYear = Column(String(15), nullable=True)
    charGender = Column(String(15), nullable=True)
    charHairColor = Column(String(15), nullable=True)
    charEyeColor = Column(String(15), nullable=True)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planetName = Column(String(120), nullable=False)
    charClimate = Column(String(15), nullable=False)
    charDiameter = Column(Integer, nullable=False)
    charPopulation = Column(Integer, nullable=True)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicleCrew = Column(String(100), nullable=True)
    charManufacturer = Column(String(15), nullable=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')