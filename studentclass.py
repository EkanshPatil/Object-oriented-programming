class student:
    def __init__(self,name,grade,marks):
        self.name = name
        self.grade = grade
        self.marks = marks

    def showmarks(self):
        return "student's marks are: {}".format(self.marks)

    def showstudentdetails(self):
        return "student's name is {}".format(self.name)
        return "student's grade is: {}".format(self.grade)

student1 = student("Ekansh",8,98)

print(student1.showmarks())
print(student1.showstudentdetails())