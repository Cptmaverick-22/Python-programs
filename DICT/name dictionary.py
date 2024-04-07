name_dict = {'Sourasish': '27.08.2004', 'Monali': '26.11.2004', 'Ankit': '07.10.2005','Sneha':'09.06.2003'}
print(name_dict)
keys = list(name_dict.keys())
keys.sort()
sorted_dict = {}
for i in keys:
    sorted_dict[i] = name_dict[i]

print("after sorting the dictionary: ")
print(sorted_dict)

name = input("Enter the name :")
if name in sorted_dict:
    print("present")
else:
    print("Name is not present")
    dob = input("Enter the date of birth to add it in the dictionary: ")
    sorted_dict[name] = dob
    print(sorted_dict)
