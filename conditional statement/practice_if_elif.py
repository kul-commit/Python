#check if the no is odd even or equal to zero

# a = int(input("Enter the no:"))

# if a ==0:
#     print("Equal to zero")
# elif a%2 == 0:
#     print("Even")
# else:
#     print("Odd")

#check the no is divisible by 2 and 3 but not 8

# no = int(input("Enter the no:"))

# if no%2==0 and no%3==0 and no%8!= 0:
#     print("No is divisible by 2 and 3 but not 8")
# else:
#     print("Not divisible")


# print the last digit of a number

# n = int(input("Enter a no"))
# last_digit = n%10

# print (f"Last digit is: {last_digit}")

# check the last digit of a number is divisible by 5

# n= int(input("Enter a no:"))

# last_digit= n%10 

# if last_digit % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5")


#calculate bill

final_amount = float(input("enter final amount:"))

if final_amount < 5000:
    discount =30
elif final_amount >=40000 and final_amount < 49999:
    discount = 25
elif final_amount >= 30000 and final_amount < 39999:
    discount = 20
elif final_amount >= 10000 and final_amount < 29999:
    discount = 10
else:
    discount =0

print(f"You got {discount}% discount")

final_bill = final_amount- (final_amount*discount/100)
print(f"Your final final bill : {final_bill}")

