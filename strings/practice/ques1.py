a= input("Enter a string: ")
count=0
# for ch in a:
#     if ch.isalpha():
#         count+= 1

for i in a:
    ascii=ord(i)
    if (ascii >=65 and ascii <=90) or (ascii>= 97 and ascii <= 122):
        count += 1
print(count)