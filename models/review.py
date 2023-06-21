#!/usr/bin/python3
"""
Review Module

This module conatins a class the defines the blue print of a Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Model

    Defines the blue print of a Review
    """
    place_id = ""
    user_id = ""
    text = ""
