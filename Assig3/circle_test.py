from circle import circle
from point import point, isclose
from math import pi, cos, sin, atan #atan is the arctan function

c1 = circle(1, 2, 5)
c2 = circle(14, 20, 10)
print(c1,c2)
p0 = point(4, 6)
print(c2.contains_point(p0))    # False
p1 = c1.get_center()
p2 = c2.get_center()
print(p0.distance(p2))          # 17.204650534085253
c2 = circle(10, 14, 10)
p2 = c2.get_center()
print(p0.distance(p2))          # 10.0
print(c2.contains_point(p0))    # True
print(c1.get_radius())          # 5
print(c2.get_radius())          # 10
print(c1.get_center().distance(p2)) # 15.0
print(c1.get_center().distance(p2) == c1.get_radius() + c2.get_radius()) # True
c3 = circle(1, 2, 15)
print(c3.get_center().distance(p2)) # 15.0
c4 = circle(4, 6, 10)
print(c3.get_center().distance(p2)) # 15.0
print(c3.get_center().distance(c4.get_center())) # 5.0
print(abs(c1.get_radius() - c2.get_radius())) # 5
print(c3.get_center().distance(c4.get_center()) == abs(c1.get_radius() - c2.get_radius())) # True
print(c3.contains_point(point(10, 14))) # True
c1.set_radius(6)
c1.set_center(0, 0)
print(c1)                       # circle(c=(0, 0), r=6)

c5 = circle()                   # Unit circle: center (0,0), radius 1

print(c5.arc_length( 90) == 1 * pi / 2) # True
print(c5.arc_length(180) == 2 * pi / 2) # True
print(c5.arc_length(270) == 3 * pi / 2) # True

alpha = atan(4 / 3) # bottom left angle of triangle((0, 0), (3, 0), (3, 4))
xx, yy = cos(alpha), sin(alpha)
### (xx,yy) = intersection of c5 with line((0,0), (3,4))

ptP = point(xx, yy)
# Due to float roundoff, this just barely makes it.
print(c5, 'contains point', ptP, c5.contains_point(ptP)) # True

# ===================================================================
# *** A common unpleasant surprise when working with floats ****

print(3/5, 4/5)                 # prints 0.6, 0.8
print((xx, yy) == (3/5, 4/5))   # False, but mathematically should be True!

# Reason this is False:
# float approximation error in the 16-th decimal place!
# xx to 0.6000000000000001 instead of 0.6,
# yy works out to 0.7999999999999999 instead of 0.8

# Attempted cure:
xx, yy = round(xx, 5), round(yy, 5)
print((xx, yy) == (3/5, 4/5)) ##True #Sigh of relief! ...

# WARNING. This is NOT a one-size-fits-all solution.

# In-depth discussion by people at various levels of expertise:
print("http://stackoverflow.com/questions/5595425/"\
      "what-is-the-best-way-to-compare-floats-for-almost-equality-"\
      "in-python")

# A more reliable way to check if two floats are close enough
# when they should be mathematically equal; use the isclose function:
#
xx,yy = cos(alpha), sin(alpha) #again
print( isclose(xx, 3/5) and isclose(yy, 4/5) )
