s  = input("Enter a string: ")

uppercase = 0
lowercase = 0
for i in s:
    if i == i.lower():
        lowercase = lowercase+1
    else:
        uppercase = uppercase+1

print("lowercase letters: ",lowercase)
print("uppercase letters: ",uppercase)