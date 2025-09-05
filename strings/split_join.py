# a = "Hello-world-this-is-python"
# words=a.split("-")
# print(words )


#join

a= ["abc",'xyc',"kul","cha",56]
new = "-".join(str(i)[::-1]for i in a) 
print(new)