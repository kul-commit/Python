#print aall the odd no

li= [2,5,3,4,6,4,6,9,7]

for i in range(0,len(li)):
    if li[i]%2!=0:
        print(li[i],end =" ")


for i in li:
    if i%2!=0:
        print(i)