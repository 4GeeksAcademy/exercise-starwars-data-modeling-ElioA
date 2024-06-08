import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email       
        }

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    DOB = Column(String(250))
    eye_color = Column(String(250))
    place_of_birth = Column(String(250))
    size = Column(String(250))
    age = Column(String(250))

    def __repr__(self):
        return f'<Character {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "DOB": self.DOB,
            "eye_color": self.eye_color,
            "place_of_birth": self.place_of_birth,
            "size": self.size,
            "age": self.age        
        }
 

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(String(250))
    location_in_galaxy = Column(String(250))
    size = Column(String(250))

    def __repr__(self):
        return f'<Planet {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "location_in_galaxy": self.location_in_galaxy,
            "size": self.size        
        }
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    def __repr__(self):
        return f'<Role {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,         
        }

  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
