
maths = int(input("enter marks 1:"))
science = int(input("enter marks 2:"))
english = int(input("enter marks 3:"))
hindi= int(input("enter marks 4:"))
Social = int(input("enter marks 5:"))

total = maths+science+english+hindi+Social

percentage = (total/500)*100

print(f"Percentage scored = {percentage}")

if percentage >= 91 and percentage <=100:
    print("Grade A")
elif percentage >=81 and percentage < 90:
    print("Grade B")
elif percentage >=71 and percentage < 80:
    print("Grade c")
elif percentage >=61 and percentage < 70:
    print("Grade d")
else:
    "Fail"