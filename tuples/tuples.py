my_tuple=(1,2,3,4,5,33)
# print(type(my_tuple))
# print(my_tuple)
# print(my_tuple[0]) 

my_list=list(my_tuple)
print(my_tuple)
my_list.append(50)
print(my_list)

my_tuple=(tuple(my_list))
print(my_tuple)