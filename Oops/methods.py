class Student():
    def __init__(self,name , marks):
        self.name=name
        self.marks= marks
    
    def welcome(self):
        print("welcome", s1.name)

    def get_marks(self):
        return self.marks


s1= Student("kul", 80)
print(s1.name)
print(s1.get_marks())