#Reverse a list

my_list = [4, -90, "Kuldeep",22.22, 100]

print(my_list[::-1]) #way 1

for i in range(0,len(my_list)):
    print(my_list[i])

for i in range(len(my_list)-1,-1,-1 ):
    print(my_list[i], end=" ") #way 2

