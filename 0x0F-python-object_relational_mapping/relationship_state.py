#!/usr/bin/python3
"""Defines the State class."""

import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# new instance of the declarative_base class.
Base = declarative_base()

# define the state class.
class State(Base):
    """Represents a state for the MySQL database."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
