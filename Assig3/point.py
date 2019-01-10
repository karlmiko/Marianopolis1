class point(object):
    """Attributes.

Instance attributes:
.x = the x-coordinate of the point object
.y = the y-coordinate of the point object

Function attributes. a.k.a. methods:
.__repr__ : the string representation of the point. Built in name.
Allows printing of any object, similar to __str__().
One of the "magic" methods in Python. YOU supply the code.

.__eq__ : returns True iff THIS point (called self) is equal in 
content with another point (if their coordinates match)

--------------------- User-defined (NOT builtin) methods--------------------
.copy: Duplicates the content of a point object) 
      Creates a new object with the same content as "self"

.distance: measures the distance from self (i.e. THIS point) to the
"other" point.

.taxicab_distance: another way to measure distance between two points
(i.e. point objects). uses so-called "Taxicab Geometry. See the docstring.
"""

# Rules for methods defined inside a class:
# 1. The first parameter must always be called self.
# 2. When the method is called, NO ARGUMENT is passed to self. That is true
#    because self is a REFERENCE (=name) for the current object. Other
#    languages (Java, C++) use the word "this" where Python uses "self"

    def __init__(self, x = 0, y = 0):
        '''Creates new point object initialized with the coordinates x, y.'''
        self.x, self.y = x, y

    def __repr__(self):
        'Converts a point to a string representation.'
        return "({:.3g}, {:.3g})".format(self.x, self.y)

    def __eq__(self, other):
        'Compares two points for equality.'
        return self.x == other.x and self.y == other.y

    def copy(self):
        "Creates a new point object with the same data as this one."
        return point(self.x, self.y)

    def distance(self, other):
        'Returns the Euclidean distance between two points.'
        def sq(num):            # local helper function
            return num ** 2

        dx, dy = self.x - other.x, self.y - other.y
        return (sq(dx) + sq(dy)) ** 0.5

    def taxicab_distance(self, other):
        """Gives the distance in the 'Taxicab Metric':
The number of units east-west + number of units north-south."""
        # Taxicab Geometry makes sense when all coordinates are integers.
        dx, dy = self.x - other.x, self.y - other.y
        return abs(dx) + abs(dy)

    # End of definition of point class
# ==================================================================
# A function to test if two floats (or one float, one int) are
# almost equal. Ref.: stackoverflow discussion group
ref = "http://stackoverflow.com/questions/5595425/"+\
    "what-is-the-best-way-to-compare-floats-for-almost-equality-in-python"
# In the Point class, the isclose() function can help when comparing
# distance between two points to some number (float). Exat == may fail!
#
# isclose() was recently added to the standard math library in Python 3,
# so you can import it from math as well.
#
def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    """rel_tol = relative tolerance, 1e-9 = 10 to the power -9,
abs_tol = absolute tolerance.
"""
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol )

# Test code.
if __name__ == '__main__': # Code below is ignored if this module
                           # is imported by another module
    # Create a list of points.
    p = [point(2, 3), point(5, 7), point(), point(1, 2)]
    
    # Prints the list of points. Note that the __repr__ method will
    # be used to convert each point into a string.
    
    print(p)

    # Use the __eq__ method to compare two points. Note that the
    # __eq__ method is sufficient to implement both == and != .

    print(p[0] != p[-1])        # True
    print(point(1, 2) == p[-1]) # True

    # Now we will examine the distance methods and the usefulness of
    # the isclose() function.
    p3, p4 = p[2:]
    print(p3.distance(p4) == 2.236)                          # False
    print(isclose(p3.distance(p4), 2.236))                   # False
    print(isclose(p3.distance(p4), 2.23607, rel_tol = 1e-5)) # True
    print(p3.taxicab_distance(p4) == 3)                      # True
    p4.x, p4.y = 3, 4
    print(p4.distance(p3) == 5.0) # True
    print(p3.taxicab_distance(p4) == 7.0) # True
    
