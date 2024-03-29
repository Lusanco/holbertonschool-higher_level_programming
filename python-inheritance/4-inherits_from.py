#!/usr/bin/python3

"""
Module Name: 4-inherits_from
Description: function that returns True if
the object is an instance of a class that
inherited (directly or indirectly) from
the specified class; otherwise False.
Authors: Lusanco
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
