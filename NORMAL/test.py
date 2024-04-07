# number list which returns sum of all even numbers
def even_num(num_list):
    sum = 0
    for i in num_list:
        if i % 2 == 0:
            sum = sum+i
    print(sum)
        
num_list = [2,5,7,8,11,34,56,8,9,35]
even_num(num_list)



