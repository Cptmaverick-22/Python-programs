n=int(input("Enter Range:"))
l=[]
h=[]
for i in range(1,n+1,2):
       l.append(i)
for j in range(0,len(l)):
        if(j%2!=0):
               h.append(-l[j])
        else:
               h.append(l[j])
print(h)