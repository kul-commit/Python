for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


for i in range (1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


for i in range(1,6):
    for j in range(i,0, -1):
        print(j, end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(5,i-1, -1):
        print(j, end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(6-i):
        print (i, end=" ")
    print()


for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(5, i-1,-1):
        print(j, end=" ") 
    print() 

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(i,0, -1):
        print(j, end=" ")
    print()

n= 5
num=1
for i in range(1, n+1):
    for j in range(i):
        print(num , end=" ")
        num= num+1
    print()