#!/bin/usr/python3
"""
Rectangle Module
"""
from base import Base

class Rectangle(Base):
     """
     Rectangle class and base subclass
     """
     def __init__(self, w, h, x=0, y=0, id=None):
         """
         Initializw a new rectangle
         """
         super().__init__(id)

         self.w = w
         self.h = h
         self.x = x
         self.y = y

     @property
     def w(self):
         """
         width getter
         """
         return self.__w

     @w.setter
     def w(self, value):
         """
         witdh setter
         """
         if not isinstance(value, int):
             raise TypeError("width must be an integer")
         if value < 0:
             raise ValueError("width must be >= 0")
         self.__w = value

     @property
     def h(self):
         """
         height getter
         """
         return self.__h

     @h.setter
     def h(self, value):
         """
         height setter
         """
         if not isinstance(value, int):
             raise TypeError("height must be an integer")
         if value < 0:
             raise ValueError("height must be >= 0")
         self.__h = value

     @property
     def x(self):
         """
         x getter
         """
         return self.__x

     @x.setter
     def x(self, value):
         """
         x setter
         """
         if not isinstance(value, int):
             raise TypeError("x must be an integer")
         if value < 0:
             raise ValueError("x must be >= 0")
         self.__x = value

     @property
     def y(self):
         """
         y getter
         """
         return self.__y

     @y.setter
     def y(self, value):
         """
         y setter
         """
         if not isinstance(value, int):
             raise TypeError("y must be an integer")
         if value < 0:
             raise ValueError("y must be >= 0")
         self.__y = value
     def area(self):

         """
         area og rectangle equation
         """
         area = self.w * self.h

         return area

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
