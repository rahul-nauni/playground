from dataclasses import  dataclass

@dataclass
class EmployeeRecord:
    name:str
    age:int
    pay:float
    role:str

emp1 = EmployeeRecord('John', 25, 5000, 'Software Engineer')
print(emp1.name)