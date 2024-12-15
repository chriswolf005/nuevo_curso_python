class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age}")

carli=Person("Carli",30)
juan=Person("Juan",25)

carli.greet()
juan.greet()