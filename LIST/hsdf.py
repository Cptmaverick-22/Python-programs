list1=[2,7,5,64,14]
for id, i in enumerate(list1):
    if(i%2!=0):
        list1.remove(id)
print(list1)