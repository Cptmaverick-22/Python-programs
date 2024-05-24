def positive(x):
    if x>0:
        return x
def negative(x):
    if x<0:
        return x
    
list1 = [1,4,6,7,8,0,-1,-5,-8,-9,-6]
positive_list = list(filter(positive,list1))
negative_list = list(filter(negative,list1))
print("positive: ",positive_list)
print("negative: ",negative_list)