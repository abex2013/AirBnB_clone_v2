#!/usr/bin/python3
"""
Place Module

This module conatins a class the defines the blue print of a Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Model

    Defines the blue print of a place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
