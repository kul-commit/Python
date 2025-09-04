#remove duplicates from list

a=[3,4,5,6,"kul","Chandni", 3,2,3,3]
b=[]

for i in a:
    if i not in b:
        b.append(i)
    
print(b)