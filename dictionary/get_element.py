x= {
    "name": "kul",
    "age": 21,
    "gender": "male",
}

k = input()
result= x.get(k)

if result is not None:
    print(result)
else:
    print("key does not exist")


# r=x.get("name")
# print(r)



# print(x["name"])
# print(x["age"])