def is_positive(x):
    if x>0:
        return x
    
list1 = [1,90,-45,-56,-67,68,43,56,-67,34]
num_list = list(filter(is_positive,list1))
print("after filter: ",num_list)