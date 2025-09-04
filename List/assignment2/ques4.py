num= int(input("enter a no:"))

a=[3,4,5,6,7,2,8,9]

for i in a[:]:
    if i%num==0:
        a.remove(i)

print(a)