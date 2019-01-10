class point(object):
    '''A class for a simple 2-dimensional point.'''
    def __init__(self, new_x, new_y):
        'The constructor method.'
        self.x = new_x
        self.y = new_y
        
    def __eq__(self, other):
        '''Implements the '==' operator.'''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''Handles conversion of a point to a str.'''
        return "POINT: " + str(self.x) + ", " + str(self.y)

    def __add__(self , other):
        '''Implements the '+' operator.'''
        return point(self.x + other.x, self.y + other.y)

    def copy(self):
        '''Makes a copy of a point. Remember, points are mutable.'''
        return point(self.x, self.y)

    def distance(self, other):
        'Euclidean distance to another point.'
        dx, dy = self.x - other.x, self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

