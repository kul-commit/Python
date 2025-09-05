a= input("enter a string")
uper_count = 0
lower_count=0
# for ch in a:
#     if ch.isupper():
#         uper_count += 1
#     elif ch.islower(): 
#         lower_count += 1
# print(uper_count)
# print(lower_count)

for ch in a:
    ascii=ord(ch)
    if ascii >=65 and ascii <=90: 
        uper_count+=1
    elif ascii>= 97 and ascii <= 122:
        lower_count+=1
print(uper_count)
print(lower_count)