# my_list= [i for i in range(1,21)]
# print(my_list)

# my_liist= [ i for i in range(1,21) if i%2==0]
# print(my_liist)\



start=int(input())
end = int(input())

my_list= [i for i in range(start,end+1) if i%2==0 and i%3==0]
print(my_list)