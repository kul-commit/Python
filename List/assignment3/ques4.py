a=[2,3,4,5,6,7,6]

# avg= sum(a)/len(a)

# print(avg)

total=0
count=0

for i in a:
    total += i
    count += 1

avg=total/count

print(avg)