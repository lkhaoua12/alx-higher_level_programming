#!/usr/bin/python3
"""Models the city table."""

import sqlalchemy
import sys
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

# creating the City class.
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
