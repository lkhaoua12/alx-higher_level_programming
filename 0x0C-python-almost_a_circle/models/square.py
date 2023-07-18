#!/usr/bin/python3
"""define the square class"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class inherite from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initize new square object"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get square size"""

        return self.width

    @size.setter
    def size(self, value):
        """set square size"""

        self.width = value
        self.height = value

    def __str__(self):
        """return string represention of square"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """update square attribute"""

        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """get dict represention of square"""

        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
