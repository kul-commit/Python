
# a=[3,2,5,4,6,8,7,1]
# b=[]

# for i in a:
#     if i%2!=0:
#         b.append(i)
# print(b)
a= [45,66,66,66,78,11]

for i in a[:]:
    if i%2==0:
        a.remove(i)
print(a)