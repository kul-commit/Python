a = input()
count = 0
for ch in a:
    if ord(ch) == 32:
        count+= 1
print(count)