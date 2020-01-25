"""
This challenge in particular took some time for me to crack.
After failing once in Dec 2019, I had another go and succeeded in Jan 2020.
This was because I had a new idea on how to calculate permutations easily while reading the
New York Times book of Mathematics. The formula it gave was very simple so easy to implement in a function.
The logic/algorithm I used here is adapted from my first attempt, but it simpler and easier to understand.
"""

import itertools
from itertools import *
import math

# Sum function
def theSum(numberArr):
    mySum = 0
    for i in numberArr:
        mySum += i
    return mySum

# Permutation function
def perms(numberArr):
    mySum = 0
    mySum = theSum(numberArr)
    numerator = math.factorial(mySum)
    over2Arr = []
    for num in numberArr:
        if num > 1:
            over2Arr.append(num)
    denominator = 1
    for num in over2Arr:
        denominator = denominator * math.factorial(num)
    answer = numerator // denominator
    return answer

# Main function
def mainLoop(digitsArr, uniqueArr, n, answerStr):
    
    #print("----------")
    
    abcdString = "ABCD"
    labels = []
    pinned2DArr = []
    
    #print("digitsArr", digitsArr)
    
    
    # Generate 2D array from digitsArr and assign labels
    for i in range(0, 4):
        if digitsArr[i] > 0:
            labels.append(abcdString[i])
            temp = []
            for j in range(0, 4):
                if j == i:
                    temp.append(digitsArr[j] - 1)
                else:
                    temp.append(digitsArr[j])
            pinned2DArr.append(temp)
            
    #print("pinned2DArr", pinned2DArr)
    #print("labels", labels)    
            
    # Permutation comparison loop
    if n == 0:
        digitsArr = pinned2DArr[len(pinned2DArr)-1]
        answerStr += labels[len(labels)-1]
    else:
        count = 0
        for array in pinned2DArr:
            count += 1
            noOfPerms = perms(array)
            #print("noOfPerms", noOfPerms)
            if n > noOfPerms:
                n -= noOfPerms
                #print("new n", n)
            elif n == noOfPerms:
                n -= noOfPerms
                digitsArr = array
                answerStr += labels[count-1]
                break                
            else:
                digitsArr = array
                answerStr += labels[count-1]
                break
                
    #print("answerStr", answerStr)
    #print("final n", n)
    #print("----------")
                
    return digitsArr, uniqueArr, n, answerStr

# Get input
userinputStr = str(input("Enter A, B, C, D, n: "))
userinputArr = userinputStr.split(" ")

digitsArr = [int(userinputArr[0]), int(userinputArr[1]), int(userinputArr[2]), int(userinputArr[3])]
n = int(userinputArr[4])

uniqueArr = []
if digitsArr[0] > 0:
    uniqueArr.append("A")
if digitsArr[1] > 0:
    uniqueArr.append("B")    
if digitsArr[2] > 0:
    uniqueArr.append("C")    
if digitsArr[3] > 0:
    uniqueArr.append("D")    

answerStr = ""
    
#print(digitsArr, n, uniqueArr)


# Run main funct in loop until sum of digits = 0
while theSum(digitsArr) > 0:
    
    # Call main function
    digitsArr, uniqueArr, n, answerStr = mainLoop(digitsArr, uniqueArr, n, answerStr)
    
print("\n" + answerStr)
    
    

"""
    if n == 0 and theSum(digitsArr) == 2:
        digitsArr = array
        answerStr += labels[count-1]
        break                  
elif n == 0 and theSum(digitsArr) > 2:
    if count == len(pinned2DArr):
        digitsArr = array
        answerStr += labels[count-1]
        break    
"""
