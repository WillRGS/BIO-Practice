import itertools
from itertools import *
import math

userinputStr = str(input("Enter A, B, C, D, n: "))
userinputArr = userinputStr.split(" ")

a = int(userinputArr[0])
b = int(userinputArr[1])
c = int(userinputArr[2])
d = int(userinputArr[3])

mainArray = []
repetitions = 1

if a > 1:
    repetitions += a
    repetitions -= 1
if b > 1:
    repetitions += b
    repetitions -= 1
if c > 1:
    repetitions += c
    repetitions -= 1
if d > 1:
    repetitions += d
    repetitions -= 1        

for i in range(0, a):
    mainArray.append("A")
for i in range(0, b):
    mainArray.append("B")
for i in range(0, c):
    mainArray.append("C")
for i in range(0, d):
    mainArray.append("D")
    
n = int(userinputArr[4]) * repetitions
print("Begin n", n)
    
total = len(mainArray)

print("mainArray", mainArray)

###

answer = []

for i in range(1, total):
    print("----")
    
    divisor = math.factorial(total-i)
    print("Divisor", divisor)
    branch = n / divisor
    branch = math.ceil(branch) - 1
    print("Branch", branch)
    
    
    for j in range(0, branch):
        if branch < len(mainArray):
            if mainArray[j] == mainArray[branch]:
                branch = j
                print("New branch", branch)
                break
    
    n = n % divisor
    if n == 0:
        n = divisor
    print("New n:", n)
    
    if len(mainArray) > 1:
        answer.append(mainArray[branch])
        mainArray.pop(branch)
    else:
        answer.append(mainArray[0])
    
    
    print("Length", len(mainArray))
    
answer.append(mainArray[0])
    
print(mainArray)

answerStr = ""
for letter in answer:
    answerStr += letter
    
print(answerStr)
    
    

'''

permArray = list(permutations(mainArray))

combArray = list(combinations(mainArray, total))

print(combArray)
print(len(combArray))



for i in range(0, total):
    print(len(list(permutations(permArray[i:total]))))


level = total
for i in range(1, total+1):
    permsAtLevel = math.factorial(total+1-i)
    if n > permsAtLevel:
        level = total+1-i
        break

print("Level", level)

branch = n // permsAtLevel

print("Branch", branch)


level = total
for i in range(1, total+1):
    perms = math.factorial(total+1-i)
    if n > (perms):
        level = total+1-i

permArray = list(permutations(mainArray[1:]))

print(permArray)
#answer = []
#for num in permArray[n-1]:
'''
    
    
