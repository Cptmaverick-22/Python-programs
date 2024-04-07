list_functions = [lambda x : x*2, lambda x : x*3, lambda x : x*4]
user = int(input("Enter the number: "))
for x in list_functions:
    print("After calling each function by a given number: ",x(user))
