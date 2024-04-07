def scaleby_10(my_list):

    for i in range(0,len(my_list)):
        my_list[i] *=10

my_list = [12,56,32,45,78,98,11,45]

print("List before calling function: ",my_list)
scaleby_10(my_list)

print("List after calling the function: ",my_list)