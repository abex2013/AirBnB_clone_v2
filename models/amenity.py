#!/usr/bin/python3
"""
Amenity Module

This module conatins a class the defines the blue print of an Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Model

    Defines the blue print of an amenity
    """
    name = ""
