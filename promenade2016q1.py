userinputStr = str(input("Please enter directions: "))

directions = ["O"]
for letter in userinputStr:
    directions.append(letter)
    
l = 1
m = 0
r = 0
s = 1

previous = [[1, 1]]

for i in range(1, len(directions)):
    #print("")
    # Find most recent left choice
    recentPosL = 0
    for j in range(0, i+1):
        if directions[j] == "L":
            recentPosL = j
            
    #print(recentPosL)
    
    # Find corresponding fraction, change l and m
    if recentPosL == 0:
        l = 1
        m = 0
    else:
        l = previous[recentPosL-1][0]
        m = previous[recentPosL-1][1]
    
    # Find most recent right choice
    recentPosR = 0
    for j in range(0, i+1):
        if directions[j] == "R":
            recentPosR = j   
            
    #print(recentPosR)
    
    # Find corresponding fraction, change r and s
    if recentPosR == 0:
        r = 0
        s = 1
    else:
        r = previous[recentPosR-1][0]
        s = previous[recentPosR-1][1]  
        
    # Calculate new fraction and store
    top = l + r
    bottom = m + s
    previous.append([top, bottom])
    
    #print("")
    
#print(previous)
print(str(previous[len(previous)-1][0]) + " / " + str(previous[len(previous)-1][1]))

'''
WRITTEN QUESTIONS:

B)

4/5 x -> LRRR

C)

999,999 L's and zero R's

D)

A promenade can only represent positive fractions. 
Negative fractions cannot be expressed by promenades.
- A negative fraction must have a negative numberator OR DENOMINATOR, which in the promenade is represented by (l+r) OR (M+S).
- l AND S begins at 1 and r AND M begins at 0. The values l and r AND M AND S can only be increased by directions, and are never decreased.
- Therefore (l+r) AND (M+S) ARE always > 0, hence a negative fraction cannot be created.
- TWO POSITIVE INTEGERS IN ADDITION CAN ONLY PRODUCE A POSITIVE INTEGER.
- THE FORMULA ADDS NON-NEGATIVE NUMBERS SO NEVER PRODUCES A NEGATIVE NUMERATOR OR DENOMINATOR.

'''
    