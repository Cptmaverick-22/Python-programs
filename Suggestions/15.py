def cel_to_far (celsius):
    return (celsius*9/5)+32

celsius_temp = [100]

far = list(map(cel_to_far,celsius_temp)) #map function takes two arguments (function name) and (list variable)

print("The farhneit temp is: ",far)