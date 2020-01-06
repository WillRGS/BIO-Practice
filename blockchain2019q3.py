### IMPORTS ###

from itertools import permutations

### SUBROUTINES ###

### MAIN PROGRAM ###

# alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

userinputStr = str(input("Please enter l and p: "))
userinputArr = userinputStr.split(" ")
l = int(userinputArr[0])
p = str(userinputArr[1]).upper()

# Get spaces remaining
spacesRemain = l - len(p)

# Get possible permutations
possiblePerms = 1

for i in range(1, spacesRemain+1):
    possiblePerms = possiblePerms * i
    
pIntArr = []
for letter in p:
    ordLetter = ord(letter)
    ordLetter -= 65
    pIntArr.append(ordLetter)
    
numbersSelect = []
for i in range(0, l):
    if i not in pIntArr:
        numbersSelect.append(i)
        
#print(numbersSelect)

#print("spacesRemain", str(spacesRemain))
#print("numbersSelect", str(numbersSelect))

# Get 2D array of all possible permutations:
permutationArr = list(permutations(numbersSelect))
#print("permutationArr", permutationArr)
#rint(permutationArr[0])

newPermArr = []
for i in range(0, len(permutationArr)):
    item = str(permutationArr[i])
    item = item.strip("(")
    item = item.strip(")")
    #print(item)
    thisArr = []
    for number in pIntArr:
        thisArr.append(number)
    
    count = 0
    while count < len(item):
        thisArr.append(int(item[count]))
        count += 3
        
    newPermArr.append(thisArr)
    

    
# Remove arrays that have alphabetic order:
for array in newPermArr:
    for i in range(0, len(array)-2):
        x = array[i]
        y = array[i+1]
        z = array[i+2]
        if (x + 1 == y) and (y + 1 == z): # Fix this
            possiblePerms -= 1
            break
            
print(possiblePerms)
    
'''
    
    
# Get limited alphabet
alphabetLim = []

for i in range(0, l):# For each letter ABCD
    alphabetLim.append(alphabet[i])
    for letter in p:
        if letter == alphabet[i]:
            alphabetLim.remove(alphabet[i])
            
alphabetLimNum = []

for letter in alphabetLim:
    coNumber = ord(letter) - 64
    
'''

'''
### WRITTEN QUESTIONS:

### MARKS:

'''




