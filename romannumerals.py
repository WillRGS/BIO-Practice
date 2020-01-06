
def toRoman(number):
    #number = int(input("Enter number between 1 and 3999: "))
    
    subtractor = 1000
    
    answer = ""
    
    while subtractor > 0:
        
        # Subtract
        while number >= subtractor:
            number -= subtractor
            if subtractor == 1000:
                answer += "M"
                #print(answer)
            elif subtractor == 500:
                answer += "D"
                #print(answer)            
            elif subtractor == 100:
                answer += "C"
                if "CCCC" in answer:
                    answer = answer[0:-4] + "CD"
                #print(answer)            
            elif subtractor == 50:
                answer += "L"
            elif subtractor == 10:
                answer += "X"
                if "XXXX" in answer:
                    answer = answer[0:-4] + "XL"
                #print(answer)            
            elif subtractor == 5:
                answer += "V"
            elif subtractor == 1:
                answer += "I"   
                if "IIII" in answer:
                    answer = answer[0:-4] + "IV"
                #print(answer)            
        
        # Replace in edge case
        if "VIV" in answer:
            answer = answer[0:-3] + "IX"
        if "LXL" in answer:
            answer = answer[0:-3] + "XC"
        if "DCD" in answer:
            answer = answer[0:-3] + "CM"
        
        # Reduce subtractor
        if subtractor == 1000:
            subtractor = 500
        elif subtractor == 500:
            subtractor = 100
        elif subtractor == 100:
            subtractor = 50
        elif subtractor == 50:
            subtractor = 10
        elif subtractor == 10:
            subtractor = 5
        elif subtractor == 5:
            subtractor = 1
        elif subtractor == 1:
            subtractor = 0   
        
    #print(answer)
    return answer
        
    '''
    if subtractor == 1000:
        #a
    elif subtractor == 500:
        #b
    elif subtractor == 100:
        #c
    elif subtractor == 50:
        #d
    elif subtractor == 10:
        #e
    elif subtractor == 5:
        #f
    elif subtractor == 1:
        #g
    '''
    
    '''
    WRITTEN QUESTIONS:
    
    B)
    
    CI
    MDCCCLXIV
    
    C)
    
    3800 more
    55 less

'''
    
'''
userinput = int(input("Enter number between 1 and 3999: "))
toRoman(userinput)
'''

more = 0
less = 0

for i in range(1, 4000):
    romani = toRoman(i)
    stri = str(i)
    
    if len(romani) > len(stri):
        more += 1
    elif len(romani) < len(stri):
        less += 1
        
print(more, less)