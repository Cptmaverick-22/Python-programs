input = [i for i in input("Enter a string: ").lower()]
con  = ''
for v in input:
    if v not in 'aeiou':
        con = con + v
print(con)



