marks={}

sub_count= int(input("enter no of subjects:"))
for _ in range(0,sub_count):
    sub_name= input("enter subject name:")
    sub_marks= int(input(f"enter marks for {sub_name}= "))
    marks[sub_name] = sub_marks

print(marks)