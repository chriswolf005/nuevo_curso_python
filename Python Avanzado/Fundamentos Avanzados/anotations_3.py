class Employee:
    name:str
    age:int
    salary:float

    def __init__(self,name:str,age:int,salary:float):
        self.name=name
        self.age=age
        self.salary=salary
    
    def introduce(self)-> str:
        return f"Hola soy {self.name}, tengo {self.age} de edad"

Employee1=Employee('Carlos',30,200000.0)
print(Employee1.introduce())