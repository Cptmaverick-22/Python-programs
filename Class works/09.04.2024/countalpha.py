input = input("enter the string: ")
count=0
if input.isalpha() == False:
    print("Invalid Input")
else:
    alphabet = []
    for i in range(26):
        alphabet.append(0)
    print(alphabet)
    for j in range(26):
        for i in range(len(input)):
            if ord(input[i]) == 65+j:
                alphabet[j] = alphabet[j] + 1
                count=j
flag=1
print(alphabet)
for i in range(count):
    if alphabet[i] != i+1:
        print('alphabet[',i,']', alphabet[i])
        flag=0
        break
if flag==1:
    print('Super ASCII')
else:
    print("NOT Super ASCII")
    