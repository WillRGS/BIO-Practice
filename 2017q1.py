# Function to combine colours into next line:
def combine(preArray):
    postArray = []
    
    for i in range(0, (len(preArray)-1)):
        
        if preArray[i] == preArray[i+1]:
            postArray.append(preArray[i])
            
        else:
            
            if preArray[i] == "R":
                
                if preArray[i+1] == "B":
                    
                    postArray.append("G")
                    
                else:
                    
                    postArray.append("B")
                
            elif preArray[i] == "B":
                
                if preArray[i+1] == "R":
                    
                    postArray.append("G")
                    
                else:         
                    
                    postArray.append("R")
                
            else:
                
                if preArray[i+1] == "B":
                    
                    postArray.append("R")
                    
                else:
                    
                    postArray.append("B")
    
    return postArray
    
    
# Get input
userInputStr = str(input("Please enter starting row: ")).upper()

while len(userInputStr) > 10:
    print("Too many characters")
    userInputStr = str(input("Please enter starting row: ")).upper()

preArray = []
for letter in userInputStr:
    preArray.append(letter)

while len(preArray) > 1:
    preArray = combine(preArray)
    
print(preArray[0])

'''
WRITTEN QUESTIONS:

B)

There are three possible rows of nine squares that generate this row.
1. RRRBBGGRG
2. GBGGRRBBB
3. BGBRGBRGR

C)

If only the colour of a single square is known on each row, there is only one solution to complete
the triangle. This is because, for every different solution of the coloured triangle, between solutions no
square has the same colour. This means that a square's colour is different for each solution. By filling in
a square on each row, there is now only one possible solution, as no two solutions can share the same colours
of the same squares - once these have been filled in there is only one solution remaining.

D)

If the first row contains ten squares, then it shares this property.

'''