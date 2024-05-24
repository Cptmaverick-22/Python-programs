elements = ['apple','banana','cherry','apple','apple','mango','pienapple','apple']
user_input = input("Enter the element: ")
for i in range(0,len(elements)):
    if elements[i] == user_input:
        print("The element is present in location: ",i)

print(f"the input appers: {elements.count(user_input)} times")