#!/usr/bin/python3
"""
Module that contains class definition of a `State`
and an instance `Base`
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class State that inherits from Base
    - links to the MySQL table `states`
    - id represents a column of auto-generated,
    uniq integer, can't be null and primary key
    - name represents a column of a string 128 chars max
    can't be null"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
