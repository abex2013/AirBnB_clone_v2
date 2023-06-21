#!/usr/bin/python3
"""
User Module

Contains the user model class that inherits BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Model

    Inherits BaseModel and is the blueprint for a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
