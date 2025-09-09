#class
class Student:
    college_name = "Nims university" #class attribute

    def __init__(self,name, marks):
      self.name=name #object attribute
      self.marks=marks

s1=Student("kul", 100)
s2=Student("cyrus", 50)

print(s1.name, s1.marks, s2.name, s2.marks)
print(s1.college_name)