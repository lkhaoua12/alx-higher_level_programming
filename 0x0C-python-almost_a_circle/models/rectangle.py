#!/usr/bin/python3
"""this module define the rectangle class"""


from models.base import Base


class Rectangle(Base):
    """class that define a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inistialze new object"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get heigh attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """set heigh attribute"""

        if not isinstance(value, int):
            raise TypeError("Height must be an integer")

        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """set x attribute"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """set y attribute"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of object"""

        return self.__width * self.__height

    def display(self):
        """print object"""

        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """return represention of object"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " + \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update attribute of object"""

        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""

        Dictionary = {}
        for x, y in vars(self).items():
            Dictionary[x.split("__")[-1]] = y
        return Dictionary
