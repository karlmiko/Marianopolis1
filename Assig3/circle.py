"""
Karl Michel Koerich , 1631968
420-LCU Computer Programming , Section 2
Wednesday , November 08
R. Vincent , instructor
Assignment 3
"""

#circle.py

from point import point, isclose
from math import pi, radians

class circle(object):
    """A simple class to represent a circle.
Attributes: Point object center, int or float number __radius
representing the radius. Note the double underscore '__' prefix
intended to hide the attributes from the client code."""

    def __init__(self, x = 0, y = 0, radius = 1):
        '''Construct a circle, which consists of a center (represented
        by a Point object) and a radius (represented by a number).'''
        self.__center = point(x, y)
        self.__radius = radius

    def get_radius(self):
        '''Gets the circle's radius.'''
        return self.__radius

    def set_radius(self, r):
        '''Sets the circle's radius.'''
        self.__radius = r

    def get_center(self):
        '''Sets the circle's center.'''
        return self.__center

    def set_center(self, x, y):
        '''Sets the circle's center.'''
        self.__center = point(x, y)

    def __repr__(self):
        """String representation of a Circle object."""
        # NOTE that since __center is a Point, it will be converted to
        # string using the __repr__ method from point. This happens
        # automatically, so we can just pass a point to format and treat
        # it as a single value.
        return "Circle(c={} r={})".format(self.__center, self.__radius)

    def __eq__(self, pt):
        '''Run implicitly when Python runs code like Circle1 == Circle2.'''
        # We construct two tuples and compare them for equality. Note that
        # the centers are compared when the two tuples are compared, which
        # means that this will also implicitly call the point class's __eq__
        # function.
        return (self.__center, self.__radius) == (pt.__center, pt.__radius)

    def circumference(self):
        return 2 * pi * self.__radius

    def arc_length(self, alpha_deg):
        ''' Gives length of arc for central angle alpha_deg DEGREES'''
        return self.__radius * radians(alpha_deg)

    def area(self):
        return pi * self.__radius ** 2

    def contains_point(self, p):
        """Returns True iff point object p is on or inside this circle."""
        return p.distance(self.__center) <= self.__radius

    def concentric_with(self, pt):
        """ Two circles are concentric iff their centers are the same."""
        return self.__center == pt.__center

    # ADD YOUR NEW METHODS AFTER THIS LINE.

    def intersects(self, other):
        '''returns True if this circle (denoted by self) and the other
           circle have at least one point in common , and False otherwise.'''
        
        dis_c1_c2 = self.__center.distance(other.__center) # Find distance from self to other
        sum_radii = self.__radius + other.__radius # Find sum or radii

        return (dis_c1_c2 < sum_radii) or (isclose(dis_c1_c2, sum_radii)) # Returns True if they intersect, otherwise False
 

    def internally_tangent(self, other):

        if not self.intersects(other):       
            
            return False # Can't possibly be tangent
        else:  
            dis_c1_c2 = self.__center.distance(other.__center)
            abs_dif_radii = abs(self.__radius - other.__radius)

            return isclose(dis_c1_c2, abs_dif_radii) 
            # Return True if the distance between their centers equals the abs value of the difference in their radii

    def externally_tangent(self, other):

        if not self.intersects(other):       
            
            return False # Can't possibly be tangent
        else:

            dis_c1_c2 = self.__center.distance(other.__center)
            sum_radii = self.__radius + other.__radius

            return isclose(dis_c1_c2, sum_radii) 
            # Return True if the distance between their centers equals the sum of the radii

    def tangent(self, other):
        '''Returns True if the circle self is either internally or externally
           tangent to the circle other.'''
        
        return self.internally_tangent(other) or self.externally_tangent(other)
        # If there is an intersection, returns True if internally or externally are True




