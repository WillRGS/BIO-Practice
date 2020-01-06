# Get input into 2D array: ###

spyArray = []
userinputStr = ""
count = 0

while userinputStr != "z -1 -1":
    userinputStr = str(input("Enter line of map: "))
    userinputArr = userinputStr.split(" ")
    
    if count == 0:
        userinputArr[0] = int(userinputArr[0])
    else:
        userinputArr[1] = int(userinputArr[1])
        userinputArr[2] = int(userinputArr[2])
        
    count += 1
    
    if "z" not in userinputArr: 
        spyArray.append(userinputArr)
    
#print(spyArray)

'''
# Find unique letters: ###
    
uniqueLetters = []

for i in range(1, len(spyArray)):
    if spyArray[i][0] not in uniqueLetters:
        uniqueLetters.append(spyArray[i][0])
        
#print(uniqueLetters)
'''

answerArr = []

'''
for letter in uniqueLetters:
    
    # Compress to shorter 2D array:
    compressedArr = []
    for row in spyArray:
        if row[0] == letter:
            compressedArr.append(row)
    
    # Collapse function:
    answerArr.append(collapse(compressedArr))
'''
totalRooms = int(spyArray[0][0])
duplicates = 0
looks = []
for roomNum in range(1, totalRooms+1):
    
    compressedArr = []
    for row in spyArray:
        if row != spyArray[0]:
            if row[1] == roomNum:
                compressedArr.append(row)
                
    #print(compressedArr)
    
    # Find look of room and append to array
    thisLook = ""
    for item in compressedArr:
        thisLook += item[0]
    
    if thisLook in looks:
        duplicates += 1
    else:
        looks.append(thisLook)
        for row in compressedArr:
            answerArr.append(row)

# Calculate new number of rooms
totalRooms -= duplicates

# Fixing rooms that previously pointed to duplicates:
# 1. Look for duplicates
# 2. If duplicate spotted, store room being pointed to
# 3. Find first row where row[1] is the duplicate room in spyArray
# 4. Find letter attached to that row
# 5. Find first row with that letter, row x
# 6. Replace faulty room with row[1] of row x

print(spyArray)
print(answerArr)

dupRooms = []
fixes = []

for row in answerArr: #1
    if row[2] > totalRooms: #2
        dupRooms.append(row[2])
        
for dupRoom in dupRooms:
    for i in spyArray:
        if len(i) > 1 and i[1] == dupRoom: #3
            dupLetter = i[0] #4
            for j in spyArray:
                if j[0] == dupLetter: #5
                    fixes.append(j[1])
                    
count = 0
for row in answerArr: #1
    if row[2] > totalRooms: #2
        row[2] = fixes[count]
        count += 1
                    

temp = [[totalRooms]]
for row in answerArr:
    temp.append(row)
    
answerArr = temp

answerArr.append(['z', -1, -1])

#print("\nAnswer:\n")
for row in answerArr:
    print(row)

    