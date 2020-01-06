
# Initialise array
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

# Get input
userinputStr = str(input("Please enter input: "))

# Split into array
userinputArr = userinputStr.split(" ")

# Assign n
n = int(userinputArr[0])

# Assign plaintext
plaintext = userinputArr[1].upper()

# Assign count
count = n - 1

# Assign ciphertext
ciphertext = []

'''

x = 26
# For loop to get 26 letter ciphertext array
for i in range(0, 26):
    ciphertext.append(alphabet[count])
    alphabet.remove(alphabet[count])
    x -= 1
    count += n
    if count > x:
        count -= (x + 1)
        
'''

while len(alphabet) > 0:
    
    if len(alphabet) == 1:
        count = 0
        
    if count > 25:
        count = count % 26
        
    ciphertext.append(alphabet[count])
    alphabet.remove(alphabet[count])
    
    for i in range(1, n):
        count += 1
        if count >= len(alphabet):
            count -= len(alphabet)
            
    #print(alphabet)
    #print(ciphertext)

# Triple ciphertext array
temp1 = ciphertext
print(temp1)
for i in range(0, 2):
    for i in range(0, len(temp1)):
        ciphertext.append(temp1[i])
    
# Initialise answer
answer = []

#print(plaintext)
#print(ciphertext)

count = 1

# Six String
sixString = ""
for i in range(0, 6):
    sixString += ciphertext[i]
print(sixString)
    

# Main loop
for plainLetter in plaintext:
    plainPosition = 0
    plainPosition = ord(plainLetter) - 65
    #print(plainPosition)
    
    cipherPosition = 0
    cipherPosition = plainPosition
    if cipherPosition < 0:
        cipherPosition = 0
    
    cipherLetter = ciphertext[cipherPosition]
    
    answer.append(cipherLetter)
    
    # Shift left by 1 or 2
    temp2 = []
    for letter in range(1, len(ciphertext)): # 1 OR 2?
        temp2.append(ciphertext[letter])
    ciphertext = temp2
    
    #print(plainLetter)
    #print(cipherLetter)
    #print(answer)
    
    # Lengthen ciphertext array if too short
    if count == 26:
        for i in temp1:
            ciphertext.append(i)   
            
    #print("c", ciphertext)
    
    count += 1
    
    

'''
FOR letter in plaintext:
    Find position of plaintext letter (1 to 26 inc.)
    Position of ciphertext letter = 2n-1
    Find ciphertext letter
    Append to answer array
    Shift ciphertext array by 1 (or 2?) to the left
'''

print("Answer: " + str(answer))