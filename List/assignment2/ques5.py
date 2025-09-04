a=[2,3,4,5,6,5,4,8,9,7]
odd=[]
even=[]

for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)