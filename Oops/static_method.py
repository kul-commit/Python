#methods that don't use the self parameter(works at class level)

class Student:
    @staticmethod #decorator
    def college():
        print("Nims")

Student.college()

