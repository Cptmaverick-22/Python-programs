import random as r
list = []
for i in range(10):
    val = r.randint(1,100)
    list.append(val)
print(list)
odd_list = []
even_list =[]
for i in range(0,len(list)):
    if list[i] % 2 == 0:
        even_list.append(list[i])
    else:
        odd_list.append(list[i])

print("even list: ",even_list)
print("odd list: ",odd_list)