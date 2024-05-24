print("vowel checker")
x = input("enter the character: ")
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'o' or x =='U':
    print("vowel")
else:
    print("consonant")

#Another Way

x = input("Enter the character: ")
if x.lower() in 'aeiou':
    print("Charcter is vowel")
else:
    print("Consonant")