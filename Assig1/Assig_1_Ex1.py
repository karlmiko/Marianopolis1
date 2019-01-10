#Karl Michel Koerich
#420-LCU Computer Programming, Section 2
#Monday, September 18
#R. Vincent, instructor
#Assignment 1

#Exercise 1

initialPoint = 0 #Lower end of the range.
endPoint = 101 #Higher end of the range.
guess = (endPoint+initialPoint)//2 #The guess will always be the average between the high and low end of the range.
numberOfGuesses = 0 #It will count how many guesses we take.
answer = '' #Creating this empty string will allow us to get into the main loop.

print('Please think of a number between 1 and 100.\n')

while (answer != 'c') and (endPoint != (initialPoint+2)): #if endpoint = initialPoint+2 so we know the answer is the value in between.
    
    answer = '' #Everytime we run the loop, it resets the value of 'answer'. 
    print('\nIs your secret number', guess, '?')
    numberOfGuesses += 1 #Increment number of guesses.
    
    while (answer != 'c') and (answer != 'h') and (answer != 'l'): #Verifies valid input.
    
        answer = input("Enter 'h' if my guess is too high, 'l' if too low, or 'c' if I am correct: ")
    
    if answer == 'h':
        
        endPoint = guess #If it's too high, we decrease the endpoint.
        print(endPoint)
        guess = (endPoint+initialPoint)//2
    
    elif answer == 'l':
        
        initialPoint = guess #If it's too low, we increase the initialPoint.
        print(initialPoint)
        guess = (endPoint+initialPoint)//2
        
print('\nGame over! I found your secret number \'', guess, '\' in', numberOfGuesses, 'guesses.')

#When I modified the range to 1-1024, I realized the largest number of guesses the program needs
# to make is 10. My guess is that 10 is the largest number of guesses since 2^10 is 1024.
#  If we choose the range to be 1-64 we will realize the largest number of guesses will be 6.
