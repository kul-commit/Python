a=[1,2,3,4,5,6,7,8,44,66]
# b=a.copy()
# b.reverse()
# print(b)

result=[]

for i in range(len(a)-1, -1,-1):
    result.append(a[i])
print(result)