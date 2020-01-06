'''
1. Get userinput //
2. Interpret userinput //
3. For each instruction, make a move if possible
4. Output final position


'''
### IMPORTS ###

import sys

### SUBROUTINES ###

def checkMove(grid, direction, plannedPos):
    
    triedSwitch = 0
    
    stuckFlag = True
    
    while stuckFlag == True:
        
        stuckFlag = False
        
        if triedSwitch == 2:
            print("All moves are not possible.")
            finalPos = []
            finalPos.append(grid[len(grid)-1][0])
            finalPos.append(grid[len(grid)-1][1])            
            print("The blocked final position is: (" + str(finalPos[0]) + ", " + str(finalPos[1]) + ")")
            sys.exit()
        
        for previousPos in grid:
            if previousPos[0] == plannedPos[0] and previousPos[1] == plannedPos[1] and triedSwitch < 2:
                print("The way is blocked")
                if instrArray[move] == "L" and triedSwitch < 1:
                    direction, plannedPos = makeMove(direction, grid, "R")
                    stuckFlag = True
                    triedSwitch += 1
                    break
                elif instrArray[move] == "R" and triedSwitch < 1:
                    direction, plannedPos = makeMove(direction, grid, "L")
                    stuckFlag = True
                    triedSwitch += 1
                    break
                elif instrArray[move] == "F" and triedSwitch < 1:
                    direction, plannedPos = makeMove(direction, grid, "L")
                    stuckFlag = True
                    triedSwitch += 1
                    break  
                elif instrArray[move] == "F" and triedSwitch < 2:
                    direction, plannedPos = makeMove(direction, grid, "R")
                    stuckFlag = True
                    triedSwitch += 1
                    break                    
                else:
                    direction, plannedPos = makeMove(direction, grid, "F")
                    stuckFlag = True
                    triedSwitch += 1
                    break    
                
    return grid, direction, plannedPos
    

def makeMove(direction, grid, instruction):
    gridLength = len(grid)
    currentPos = grid[gridLength-1]
    plannedPos = []
    
    if instruction == "L":
        
        if direction == "U":
            direction = "L"
        elif direction == "L":
            direction = "D"
        elif direction == "D":
            direction = "R"
        else:
            direction = "U"
        
    elif instruction == "R":
        
        if direction == "U":
            direction = "R"
        elif direction == "R":
            direction = "D"
        elif direction == "D":
            direction = "L"
        else:
            direction = "U"
    
    if direction == "D":
        plannedPos.append(currentPos[0])
        plannedPos.append(currentPos[1]-1)
        
    elif direction == "L":
        plannedPos.append(currentPos[0]-1)
        plannedPos.append(currentPos[1])        
        
    elif direction == "R":
        plannedPos.append(currentPos[0]+1)
        plannedPos.append(currentPos[1])        
        
    elif direction == "U":
        plannedPos.append(currentPos[0])
        plannedPos.append(currentPos[1]+1)        
        
    plannedPos.append(0)
    
    return direction, plannedPos   
    

### MAIN PROGRAM ###

grid = []
    
t = 0
instructions = ""
m = 0

# Get user input
while (t < 1) or (t > 100) or (m < 1) or (m > 10000):
    userinput = input("Please enter: t, instructions, m: ")
    userinput = userinput.split(" ")
    t = int(userinput[0])
    instructions = userinput[1]
    m = int(userinput[2])
    
# Initialise grid and direction
direction = "U"

# Format: xPos, yPos, age
grid.append([0, 0, 0])
# grid[0].append()

# Get instructions into array
instrArray = []
for letter in instructions:
    instrArray.append(letter.upper())
    
appender = 0
while m > len(instrArray):
    instrArray.append(instrArray[appender])
    appender += 1

# Mainloop iterating through array
for move in range(0, m):
    
    direction, plannedPos = makeMove(direction, grid, instrArray[move])  
    grid, direction, plannedPos = checkMove(grid, direction, plannedPos)
            
    grid.append(plannedPos) # MAKE MOVE
    
    print(grid)       
    
    # Update ages of trail
    for position in grid: 
        position[2] += 1 # Update the age
        
    if grid[0][2] == t:
        temp = []
        for i in range(1, len(grid)):
            temp.append(grid[i])
        grid = temp
    
finalPos = []
finalPos.append(grid[len(grid)-1][0])
finalPos.append(grid[len(grid)-1][1])
print("The final position is: (" + str(finalPos[0]) + ", " + str(finalPos[1]) + ")")


'''
z = 1

class myClass:
    x = 10 + z
    
array = []
    
for i in range(0, 5):
    array.append(myClass())
    
print(array[0].x)
'''
    