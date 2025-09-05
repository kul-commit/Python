a= input("enter a string: ")
result=""

for ch in a:
    ascii= ord(ch)
    if ascii >=97 and ascii <= 122:
        new= ascii-32
        char= chr(new)
        result = result+char
    else:
        result += ch
 
print(result)