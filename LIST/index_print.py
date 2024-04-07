# Write down a python code to print index at which a particular value exists , if the value exists at multiple location in the list then print
#all the indices. Also count the number of the times the value is repeated.

elements = ['apple','banana','cherry','apple','apple','mango','pienapple','apple']
user_input = input("Enter the element: ")
for i in range(0,len(elements)):
    if elements[i] == user_input:
        print("The element is present in location: ",i)

print(f"the input appers: {elements.count(user_input)} times")