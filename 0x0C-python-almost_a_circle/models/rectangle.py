#!/usr/bin/python3
'''Rectangle class.'''

from base import Base


class Rectangle(Base):
    '''Rectangle class that defines a rectangle.'''

    def __init__(self, width: int, height: int, x: int = 0, 
                 y: int = 0, id: int = None):
        '''Initialize a rectangle instance.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        '''Return the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value: int):
        self.validate_integer("width", value, is_positive=True)
        self.__width = value

    @property
    def height(self) -> int:
        '''Return the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value: int):
        self.validate_integer("height", value, is_positive=True)
        self.__height = value

    @property
    def x(self) -> int:
        '''Return the x coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value: int):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self) -> int:
        '''Return the y coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value: int):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name: str, value: int, 
                         is_positive: bool = False):
        '''Validate that value is an integer and meets specified conditions.'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if is_positive and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif not is_positive and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self) -> int:
        '''Return the area of the rectangle.'''
        return self.width * self.height

    def display(self) -> None:
        '''Print the rectangle using `#`.'''
        print(
            ('\n' * self.y) +
            (' ' * self.x + '#' * self.width + '\n') * self.height,
            end=''
        )

    def __repr__(self) -> str:
        '''Return a string representation of the rectangle.'''
        return (
            f"[{type(self).__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )
