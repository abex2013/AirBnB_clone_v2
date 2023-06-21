#!/usr/bin/python3
"""City Module

This module conatins a class the defines the blue print of a city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Model

    Defines the blue print of a city
    """
    state_id = ""
    name = ""
