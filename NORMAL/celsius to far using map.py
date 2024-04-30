def cel_to_far (celsius):
    return (celsius*9/5)+32

celsius_temp = [100,200]

far = list(map(cel_to_far,celsius_temp))

print("The farhneit tem is: ",far)