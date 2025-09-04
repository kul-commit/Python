a=[2,3,4,5,22,33,4,56,90]

num= int(input("enter a no:"))

if num in a:
    index= a.index(num)
    print(index)
else:
    print(-1)