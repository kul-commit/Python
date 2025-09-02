"""
calculate the sum of 5 subject and find percentage
"""

sub1 = int(input("enter the subject:"))
sub2 = int(input("enter the subject:"))
sub3= int(input("enter the subject:"))
sub4 = int(input("enter the subject:"))
sub5 = int(input("enter the subject:"))

sum = sub1 + sub2 + sub3 + sub4 + sub5
total = 500

percentage =  (sum/ total) * 100

print(f"Total sum is : {sum}")
print(f"Total percentage is: {percentage}")