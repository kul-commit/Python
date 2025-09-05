a= input()
result=""
for i in a:
    ascii= ord(i)
    if ascii >= 65 and ascii <= 90:
        new =ascii+32
        char = chr(new)
        result += char
    else:
        result += i
print(result)
