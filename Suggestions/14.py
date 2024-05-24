string = input("Enter a string: ")
vowels = 0
consonants = 0
for i in string:
    if i.lower() in 'aeiou':
        vowels+=1
    else:
        consonants+=1
print("The number of vowels: ",vowels)
print("The number of consonants: ",consonants)