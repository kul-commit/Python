# print sum of all elements in list

a= [2,4,3,6,5,7,8]
summ=0

for i in a:
    summ=summ+i 
print(summ )


for i in range(0, len(a)):
    summ= summ+a[i]
print(summ)


a= [2,4,3,6,5,7,8]  
count=0
for i in a:
    if i%2==0:
        count=count+1
print(count)

a= [2,4,3,6,5,7,8, 10]
count=0
for i in a:
    if i%2==0 and i%5==0:
        count = count+ 1
print(count)

a= [2,4,3,6,5,7,8, 10]
sum= 0
for i in a:
    if i%2==0:
        sum=sum+i
print(sum)

a= [2,4,3,6,5,7,8, 12,24,10]
sum = 0
for i in range(0,len(a)):
    if a[i]%3==0 and a[i]%4==0:
        sum=sum+a[i]
print(sum)


a= [2,4,3,6,5,7,8, 12,24,10]
largest = a[0]
for i in range(0,len(a)):
    if a[i] > largest:
        largest=a[i]
print(largest)

a=[34, 65,35,23,90,78,23]
largest = a[0]

for i in a:
    if i > largest:
        largest= i
print(largest)