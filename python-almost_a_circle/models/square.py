#!/usr/bin/python3

"""
Module: square
Descrip: Square class
Authors: Lusanco
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
