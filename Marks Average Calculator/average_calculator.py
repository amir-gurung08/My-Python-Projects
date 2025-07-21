class Student:
    def __init__(self, name, english, maths, science):
        self.name = name
        self.english = english
        self.maths = maths
        self.science =science

    def average(self):
        average = (self.english + self.maths + self.science) / 3
        print(average)

name = input("Enter Name of the student: ")
marks1 = int(input("Enter the marks of English: "))
marks2 = int(input("Enter the marks of Maths: "))
marks3 = int(input("Enter the marks of Science: "))

s1 = Student(name,marks1,marks2,marks3)

s1.average()