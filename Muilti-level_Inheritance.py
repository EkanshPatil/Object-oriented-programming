class person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age

    def show(self):
        return f"name: {self.name}"
    
class employ(person):
    def __init__(self,name,age,salary):
        super().__init__(self,name,age)
        self.salary = salary

    def show_salary(self):
        return f"Salary: {self.salary}"
    
class manager(employ):
    def __init__(self,name,age,salary,department):
        super().__init__(self,name,age,salary)
        self.department = department
    
    def show_department(self):
        return f"Department: {self.department}"
    
p = person("Ekansh",14)
e = employ("Ekansh",14,10500)
m = manager("Ekansh",14,10500,"Engineering")
print(m.show())
print(m.show_salary())
print(m.show_department())