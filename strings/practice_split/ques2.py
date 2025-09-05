a = "pyhton is good"
words = a.split()
result = " ".join(i.capitalize() for i in words)

print(result)
a = "pyhton is good"
words = a.split()
result = " ".join(i[::-1] for i in words)

print(result)