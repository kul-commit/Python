myset={1,2,3,45,6,4,2}

num = int(input("enter a number"))

# found = False
# for i in myset:
#     if i==num:
#         found=True
# if found :
#     print("yes")
# else:
#     print("No")

if num in myset:
    print("yes")
else:
    print("no")