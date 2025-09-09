class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_average(self):
        sum= 0
        for i in self.marks:
            sum = sum+ i
        print(f"hi ,{self.name} your avg marks is {sum/3}")


s1= Student("kul", [27,30,28])
print(s1.name,s1.marks) 
s1.get_average()