import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    skin_color = Column(String(100), nullable=False)
    eye_color = Column(String(100), nullable=False)

class FavouritePlanet(Base):
    __tablename__ = 'favourite_planet'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))

class FavouriteCharacter(Base):
    __tablename__ = 'favourite_character'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_character = Column(Integer, ForeignKey('character.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')