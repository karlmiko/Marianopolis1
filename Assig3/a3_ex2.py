"""
Karl Michel Koerich , 1631968
420-LCU Computer Programming , Section 2
Wednesday , November 08
R. Vincent , instructor
Assignment 3
"""

# a3_ex2.py

from circle import circle
from point import point

def test_func_circle(c_main, c_list, n):
	""" Print a table with the results of the comparisons between
	c_main and the other circles.
	"""

	print("Test {}:".format(str(n)))
	print("{:>28}{:>14}{:>14}{:>14}{:>14}".format(str(c_main), "Intersects?", "Has tangent?", "Externally?", "Internally?"))
	print()

	for c in c_list:
		print("{:>28}{:>14}{:>14}{:>14}{:>14}".format(str(c), str(c.intersects(c_main)), str(c.tangent(c_main)), str(c.externally_tangent(c_main)), str(c.internally_tangent(c_main))))
	print()


### Test 1 ###

c_main = circle(0, 0, 1)
# Different circles to relate to c_main
c1 = circle(8, 0, 3)
c2 = circle(5, 0, 9) 
c3 = circle(5, 0, 4)
c4 = circle(3, 0, 4)
c5 = circle(0, 0, 1)
c_list = [c1, c2, c3, c4, c5]
test_func_circle(c_main, c_list, 1) 

### Test 2 ###

c_main = circle(5, 2.4, 3.5)
# Different circles to relate to c_main
c1 = circle(0, 0, 1)
c2 = circle(5, 6.1, 0.2)
c3 = circle(5, 5.2, 0.7)
c4 = circle(6.7, 5.2, 0.15)
c5 = circle(0, 2.4, 1.5)
c_list = [c1, c2, c3, c4, c5]
test_func_circle(c_main, c_list, 2)

### Test 3 ###

c_main = circle(8, 7.1, 5.5)
# Different circles to relate to c_main
c1 = circle(-2, 7.1, 4.5)
c2 = circle(8, 7.1, 5.6)
c3 = circle(6.9, 7.2, 4.3954639) # To test decimal points
c4 = circle(6.9, 7.2, 4.395463898) # To test decimal points
c5 = circle(7, 5.6, 1.5)
c_list = [c1, c2, c3, c4, c5]
test_func_circle(c_main, c_list, 3)


### Decimal points test seen above ###
p1 = c_main.get_center()
p2 = c3.get_center()

d = p1.distance(p2)
r2 = 5.5 - d
print("Radius C3 = " + str(r2)) #Value of r2 just that c_main and c3 such that they are internally tangent.
