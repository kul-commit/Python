my_list= [2,4,4,5,4, 5,6,3,9]
old = int(input("old no"))
new= int(input("new no"))

for i in range(0, len(my_list)):
    if my_list[i]==old:
        my_list[i]= new
print(my_list)
