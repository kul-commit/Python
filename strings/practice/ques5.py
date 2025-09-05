a = input()
# lower=""
# upper=""
# for ch in a:
#     ascii = ord(ch)
#     if ascii >= 65 and ascii <= 90:
#         new = ascii + 32
#         char = chr(new)
#         lower += char
#     elif ascii>= 97 and ascii <= 122:
#         new_ascii = ascii -32
#         char = chr(new_ascii)
#         upper += char
#     else:
#         lower+=ch
#         upper+= ch
# print(lower)
# print(upper)
new_string=""
for ch in a:
    ascii= ord(ch)
    if ascii >= 65 and ascii <= 90 :
        new= ascii+32 
        char= chr(new)
        new_string += char
    elif   ascii>= 97 and ascii <= 122:
        new= ascii-32
        char=chr(new)
        new_string += char
    else:
        new_string += ch
print(new_string)


