import math

debt = 100
interest = -1
repay = -1
totalRepaid = 0
month = 1

# print(round(5.48, 2))

'''
x = 2.3456
x = round(x, 3)
print(x)
x = math.ceil(x * 100)
print(x)
'''

while interest < 0 or interest > 1 or repay < 0 or repay > 1:
    userinputStr = str(input("Please enter userinput: "))
    userinputArr = userinputStr.split(" ")
    interest = userinputArr[0]
    interest = int(interest)
    interest = interest / 100
    repay = userinputArr[1]
    repay = int(repay)
    repay = repay / 100
    
while debt > 0:
    print("Month: " + str(month))
    print("Remaining debt: " + str(debt))
    
    thisInterest = debt * interest
    thisInterest = round(thisInterest, 3)
    thisInterest = math.ceil(thisInterest * 100) / 100
    debt += thisInterest
    print("This interest: " + str(thisInterest))
    print("Debt after: " + str(debt))
    
    thisRepay = debt * repay
    thisRepay = round(thisRepay, 3)
    thisRepay= math.ceil(thisRepay * 100) / 100
    if thisRepay < 50:
        thisRepay = 50
    if thisRepay > debt:
        thisRepay = debt
    totalRepaid += thisRepay
    debt = debt - thisRepay
    print("This repay: " + str(thisRepay))
    
    month += 1

print(round(totalRepaid, 2))

### WRITTEN QUESTIONS ###

