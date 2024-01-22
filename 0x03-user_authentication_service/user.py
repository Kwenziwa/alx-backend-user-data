#!/usr/bin/env python3
# Author: Kwenziwa Lizwi Khanyile
# Date Created: 2024-01-22
# Description: In this task you will create a
# SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

"""
Users model

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ Represents user object/table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
