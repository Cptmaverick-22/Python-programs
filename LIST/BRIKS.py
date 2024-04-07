# Write a program which defines a list of countries that are a member of  (BRICS), check whether a country is a member of BRICS or not.
BRICS = ['Brazil','Russia','India','China','South Africa','Egypt','Ethiopia','Iran','United Arab Emirates']
brics_lower =[]
for i in BRICS:
    brics_lower.append(i.lower())

country = input("Enter the Country: ")
if country.lower() in brics_lower:
    print("Present")
else:
    print("Absent")