x= {
   "english": 67,
   "hindi": 89,
   "maths": 56,
   "science": 34,
}

# for i in x.keys():
#     print(x[i])
total=0
for i in x.values():
    total += i

print(total)