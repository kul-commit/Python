#no is positive or negative 
# num = int(input("Enter number :"))

# if(num >=0):
#     print("Number is positive")
# else:
#     print("Number is negative")

#check char is vowel or a consonants

#char = input("Enter a character:")

# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
#     print("Vowels")
# else:
#     print("Consonants")


# First no is divisible bye  the second

# a = int(input("Enter no 1:"))
# b = int(input("Enter no 2:"))

# if a % b ==0:
#     print("Divsible")
# else:
#     print("Not divisible")


# attendance

classes_held = int(input("Enter total no of classes held:"))
class_attended = int(input("Class attended:"))

percentage = (class_attended / classes_held)*100
print(f"Total percentage : {percentage: .2f}")

if percentage >= 75:
    print("Allowed")
else:
    print("Not Allowed")