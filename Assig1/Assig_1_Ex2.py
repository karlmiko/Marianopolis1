#Karl Michel Koerich
#420-LCU Computer Programming, Section 2
#Monday, September 18
#R. Vincent, instructor
#Assignment 1

#Exercise 2

def pricePlan(letter, planX, minutes): #This function receives a plan and the minutes and returns the total price.

	if minutes[0] > planX[3]: #If daytime mins are higher than the free value, set a new value for daytime and charge.
		
		minutes[0] = minutes[0] - planX[3]

	else:

		minutes[0] = 0

	totalPrice = 0 #This variable will have the total price of the plan.

	for i in range(0,3): #Multiplies price with minutes (in cents).
		
		totalPrice += (minutes[i]*planX[i]) #Adds to total price.
		
	print('Plan', letter, 'costs', totalPrice/100, 'dollars.') #Divides by 100 to show price in dollars.

	return totalPrice

PLAN_A = [25, 15, 20, 100] #Day-0 Eve-1 Wee-2 (price in cents) MinFree-3.
PLAN_B = [45, 35, 25, 250] #Day-0 Eve-1 Wee-2 (price in cents) MinFree-3.

times = ['daytime','evening','weekend']
minutes = [] #Day-0 Eve-1 Wee-2 / This list will receive the minutes.

for i in range (0,3): #Reads the minutes and places them into 'minutes'.
	
	isInt = False

	while isInt == False: #While the input is not a numeric value, it asks again for it.

		inputMinutes = input('Number of ' + times[i] + ' minutes? ')
		isInt = inputMinutes.isnumeric()
		
	minutes.append(int(inputMinutes))

priceA = pricePlan('A', PLAN_A, minutes) #The price with plan A is set.
priceB = pricePlan('B', PLAN_B, minutes) #The price with plan B is set.

if (priceA - priceB) == 0: #Verifies if they are equal or if A < B.
	
	print('Plan A and B are the same price.')

elif (priceA - priceB) < 0:

	print('Plan A is cheaper.')

else:

	print('Plan B is cheaper.')

	
