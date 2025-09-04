age = int(input("enter your age:"))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


#which no is greater 

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))

if num1 > num2:
    print("Num 1 is greatest")
else:
    print("Num 2 is gratest")


#find no is odd or even

a = int(input("Enter no :"))

if a %2 == 0:
    print("No. is Even")
else:
    print("No is odd")



phy = int(input("Enter physics marks:"))
chem = int(input("Enter chem marks:"))

if phy >= 33 and chem >= 33:
    print("PAssed")
else:
    print("failed")