class fraction(object):
    '''Class to represent exact fraction arithmetic.

    Remember that floating point numbers have limited precision. They
    can't represent arbitrarily large or small numbers, and have a
    limited number of significant digits. Because integers in Python
    have an unlimited range, it is possible to represent any rational
    number as a ratio of two integers. This class exploits this.
    '''
    def __init__(self, num, den = 1):
        '''Construct a fraction object.'''
        def gcd(a, b):          # local function
            '''Compute the greatest common divisor of integers
            a and b.'''
            while b != 0:
                a, b = b, a % b,
            return a
        # Make sure num and den are integers.
        num = int(num)
        den = int(den)
        # Disallow zero denominator.
        if den == 0:
            raise ValueError("Can't have a zero denominator!")
        # Reduce fraction to lowest terms. This is done in the
        # constructor to avoid code duplication.
        div = gcd(num, den)
        self.__num = num // div
        self.__den = den // div

    def __repr__(self):
        '''Convert a fraction object to a string.'''
        return 'fraction({}, {})'.format(self.__num, self.__den)

    def __add__(self, other):
        '''Add two fraction objects, yielding a new fraction object.'''
        
        #----3.1----#
        #Adding an int to a fraction
        if not isinstance(other, fraction):
            other = fraction(other)
        #----3.1----#

        new_num = self.__num * other.__den + self.__den * other.__num
        new_den = self.__den * other.__den
        return fraction(new_num, new_den)

    #----3.2----#
    def __sub__(self, other):
        '''Sub two fraction objects, yielding a new fraction object.'''
        
        #Sub an int to a fraction
        if not isinstance(other, fraction):
            other = fraction(other)

        new_num = self.__num * other.__den - self.__den * other.__num
        new_den = self.__den * other.__den
        return fraction(new_num, new_den)

    def __truediv__(self, other):
        if not isinstance(other, fraction):
            other = fraction(other)
        new_num = self.__num * other.__den
        new_den = self.__den * other.__num
        return fraction(new_num, new_den)
    #----3.2----#

    #----2.4----#
    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        else:
            return str(self.__num) + '/' + str(self.__den)
    #----2.4----#

    #----2.7----#
    def __eq__(self, other):
        return self.__num == other.__num and self.__den == other.__den    
    #----2.7----#

    #----3.1----#
    def __mul__(self, other):

        if not isinstance(other, fraction):
            other = fraction(other)
        new_num = self.__num * other.__num
        new_den = self.__den * other.__den
        return fraction(new_num, new_den)
    #----3.1----#
    
if __name__ == "__main__":
    # Run the test code. When your class is complete, all of these
    # tests should pass.
    a = fraction(1, 2)
    b = fraction(1, 3)
    assert repr(a) == 'fraction(1, 2)'
    assert repr(a + b) == 'fraction(5, 6)'
    assert str(a) == '1/2'         # requires __str__
    assert str(a + b) == '5/6'     # requires __str__
    c = fraction(5, 1)
    assert str(c) == '5'           # requires __str__
    print("__str__ OK")
    assert a + b == fraction(5, 6) # requires __eq__
    assert a != b                  #
    print("__eq__ OK")
    assert a * b == fraction(1, 6) # requires __mul__
    assert a * fraction(5, 1) == fraction(5, 2)     # requires __mul__
    print("All OK")
