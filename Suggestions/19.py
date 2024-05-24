def sorting(list1,list2):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                list2[j],list2[j+1] = list2[j+1],list2[j]

list1 = [int(x) for x in input("Enter the elements: ").split()]
list2 = [int(x) for x in input("Enter the elements: ").split()]
sorting(list1,list2)
list1.extend(list2)
list1.sort()
print(list1)
