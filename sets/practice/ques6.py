a={1,2,3,4,5}
b={2,3,1,4,22,43,4}

result= a.intersection(b)

if len(result)==0:
    print("Both sets have nothing common")
else:
    print("Sets have something common")

print(result)