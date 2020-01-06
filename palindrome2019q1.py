def case1(numStr, length, halfLength, nextNumStr):
    if length % 2 == 0:
        # Number has even number of digits
        for i in range(0, halfLength):
            nextNumStr += numStr[i]
        
        nextNumInt = int(nextNumStr)
        nextNumInt += 1
        nextNumStr = str(nextNumInt)
    
        for i in range(1, halfLength+1):
            nextNumStr += nextNumStr[halfLength - i]
        
        print("The next number is: " + nextNumStr)  
    
    else:
        # Number has odd number of digits
        halfLength += 1
        
        for i in range(0, halfLength):
            nextNumStr += numStr[i] 
            
        nextNumInt = int(nextNumStr)
        nextNumInt += 1
        nextNumStr = str(nextNumInt)   
        
        for i in range(2, halfLength+1):
            nextNumStr += nextNumStr[halfLength - i]
            
        print("The next number is: " + nextNumStr)    
    

num = int(input("Please enter palindromic number: "))

numStr = str(num)
length = len(numStr)
halfLength = length // 2

nextNumStr = ""

if length % 2 == 0:
    # Number is even
    for i in range(1, halfLength+1):
        # ...
        print("")
        
    
else:
    # Number is odd

# case1(numStr, length, halfLength, nextNumStr)
