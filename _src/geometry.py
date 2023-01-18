"""
This module is containing two classes of two geometry shapes:

* :py:class:`circle()`
* :py:class:`cylinder()`

:py:class:`circle()` class is containing :func:`circle.perimeter()` and :func:`circle.area()` functions.

:py:class:`cylinder()` class is containing :func:`cylinder.surface_area()` and :func:`cylinder.volume()` functions

"""


class circle:

    """
    This is circle class. We can write project description here.

    param radius: Radius of a cylinder
    :type radius: float, int
    """

    def __init__(self, radius):
        """
        Class constructure
        """
        self.r = radius

    def perimeter(self):
        """
        This method calculates the perimeter of the circle.

        :return: Perimeter
        :rtype: float
        """
        return 2*3.14*self.r

    def area(self):
        """
        This method calculates the area of the circle

        :return: Area
        :rtype: float
        """
        return 3.14*self.r**2


class cylinder:
    """
    This is a cylinder class. It stores radius and length of a cylinder.

    :param radius: Radius of a cylinder
    :type radius: float, int
    :param height: Height of a cylinder
    :type height: float

    """

    def __init__(self, radius, height):
        """
        Class constructure
        """
        self.r = radius
        self.h = height

    def surface_are(self):
        """
        This method calculates the surface area

        :return: Surface of the cylinder
        :rtype: float
        """
        return 2*3.14*self.r*(self.h+self.r)

    def volume(self):
        """
        This method is part of :py:class:`.geometry.cylinder()` class and calculates Volume of it.

        :return: Volume of the cylinder
        :rtype: float
        """
        return 3.14*self.h*self.r**2