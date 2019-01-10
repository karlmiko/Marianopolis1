#TicTacToe_0_2.py

import random

#Functions

def verifyWinner(xOrO): #See if somebody won.

    for listOf3 in possiblities: #Runs over list of possible winning sequences.

        countTo3 = 0

        for strInListof3 in listOf3:

            inputI = int(strInListof3[0])
            inputJ = int(strInListof3[1])

            if matrix[inputI][inputJ] == xOrO:
                countTo3 += 1

        if countTo3 == 3:

            return True

    return False


def machineCoord(): #Positions that machine will priorize.
    
    priorities = ['33', '11', '15', '55', '51', '35', '13', '31', '53']

    for coord in priorities:

        inputI = int(coord[0])
        inputJ = int(coord[1])

        if matrix[inputI][inputJ] == ' ':
            
            return coord


def verifyPossibleWinningMove(playerXorO, machineXorO, times_func_called): #Most important function, artificial inteligence of machine.

#This function verifies if machine has a possibility of winning.
#If machine is not able to win, the function will be recalled inside itself to verify if user has a chance to win.
#If nobody can win in the next move, it win call machinceCoord which will look for a empty space to play.

    for listOf3 in possiblities:

        countTo2 = 0 #This variable is the most important one, it will count to 2 if there is a winning possibility.
       
        for strInListof3 in listOf3:


            inputI = int(strInListof3[0])
            inputJ = int(strInListof3[1])

            if matrix[inputI][inputJ] == machineXorO:
                
                countTo2 += 1
                continue

            elif matrix[inputI][inputJ] == playerXorO:
                
                countTo2 += 5 #Big random number so its != 2.

            elif verifyEmptyCoordinate(inputI, inputJ) is True:

                nextMove = str(inputI) + str(inputJ)

        if countTo2 == 2:

            return nextMove

    if times_func_called == 1:

        nextMove = verifyPossibleWinningMove(machineXorO, playerXorO, 2) #Second time, it will verify if user can win, playerXorO and machineXor0 will be inverted.
        return nextMove #We have to return again because the return from second time func returns to the first time func.

    return machineCoord() #If both tests fail, it will return machineCoord().
    

def printBoard(): #This function prints the board.

    print()
    for n in range(0, 6):
        print(matrix[n][0], matrix[n][1], matrix[n][2], matrix[n][3], matrix[n][4], matrix[n][5])

def verifyCoordinatesInput(): #This function reads the coordinates and returns when they are valid (i, j).

    while True:
    
        toReplaceIandJ = ''
        coordinatesInput = ''

        while len(coordinatesInput) != 2: #The length is expected to be equal 2.

            coordinatesInput = input("\nWhat coordinate? Capital letter + Number, example 'A1': ")

        inputI = coordinatesInput[1]
        inputJ = coordinatesInput[0]

        if inputI == '1':
            toReplaceIandJ = toReplaceIandJ + '1'
        if inputI == '2':
            toReplaceIandJ = toReplaceIandJ + '3'
        if inputI == '3':
            toReplaceIandJ = toReplaceIandJ + '5'

        if inputJ == 'A':
            toReplaceIandJ = toReplaceIandJ + '1'
        if inputJ == 'B':
            toReplaceIandJ = toReplaceIandJ + '3'
        if inputJ == 'C':
            toReplaceIandJ = toReplaceIandJ + '5'

        if len(toReplaceIandJ) == 2: 
            return toReplaceIandJ

def verifyEmptyCoordinate(inputI, inputJ): #It verifies if the coordinate is empty

    if matrix[inputI][inputJ] == ' ':
        return True

    return False

def playAgain(): #Asks if user wants to play again

    while True:

        keepPlaying = input('\nDo you want to play again? \'y\' for YES and \'n\' for NO: ')

        if (keepPlaying != 'y') and (keepPlaying != 'n'):
            print("\nPlease introduce a valid character.")

        if (keepPlaying == 'y'):
            return True

        if (keepPlaying == 'n'):
            return False

def defineXorO(): #Asks if user wants 'o' or 'x'

    while True:
            
        playerXorO = input('\nDo you want X or O? \'x\' for X and \'o\' for O: ')

        if (playerXorO != 'x') and (playerXorO != 'o'):
            print("\nPlease introduce a valid character.")

        else: 
            return playerXorO

#Game starts

keepPlaying = True #While this is true, we will play, again and again.
possiblities = [['11', '31', '51'], ['13', '33', '53'], ['15', '35', '55'], ['11', '13', '15'], ['31', '33', '35'], ['51', '53', '55'], ['11', '33', '55'], ['51', '33', '15']]
pointsUser, pointsMachine = 0, 0 #Score of the game.

while keepPlaying == True:
    
    playerXorO = defineXorO()

    if playerXorO == 'x':
        machineXorO = 'o'
    else:
        machineXorO = 'x'

    matrix = [['#', 'A', ' ', 'B', ' ', 'C'], ['1', ' ', '|', ' ', '|', ' '], [' ', '-', '-', '-', '-', '-'], ['2', ' ', '|', ' ', '|', ' '], [' ', '-', '-', '-', '-', '-'], ['3', ' ', '|', ' ', '|', ' ']]
    #The board of the game is set

    whoStarts = random.randint(0,1) #0 or 1 to see who starts.
    plays = 3 #Variable just used to set who starts depending on the number of the line above.
    winner = False #winner will become true once somebody wins.
    
    while plays < 12 and winner is False:

        if plays % 2 == whoStarts:

            printBoard()
            goodCoordinate = False

            while goodCoordinate == False:
                coordinatesInput = verifyCoordinatesInput()
                inputI = int(coordinatesInput[0])
                inputJ = int(coordinatesInput[1])
                goodCoordinate = verifyEmptyCoordinate(inputI, inputJ)

            matrix[inputI][inputJ] = playerXorO
            plays += 1

            if verifyWinner(playerXorO) is True:
                printBoard()
                pointsUser += 1
                print('\nCongratulations, you won! The score is: You', pointsUser, 'x', pointsMachine, 'Machine')
                winner = True

        else:
            
            coordinatesMachine = verifyPossibleWinningMove(playerXorO, machineXorO, 1)
            inputI = int(coordinatesMachine[0])
            inputJ = int(coordinatesMachine[1])

            matrix[inputI][inputJ] = machineXorO
            plays += 1
            
            if verifyWinner(machineXorO) is True:
                printBoard()
                pointsMachine += 1
                print('\nToo bad, you lost! The score is: You', pointsUser, 'x', pointsMachine, 'Machine')
                winner = True

    if plays == 12 and winner is False:
        printBoard()
        print('\nIt\'s a tie, nobody won! The score is: You', pointsUser, 'x', pointsMachine, 'Machine')

    keepPlaying = playAgain()

print("\nThanks for playing. Bye bye!")