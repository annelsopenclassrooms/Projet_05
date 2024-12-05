class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def display_details(self):
        print(f"{self.name} a {self.age}")

class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def display_details(self):

        super().display_details()
        print(f"Salaire: {self.salary}")
        
p = Person("Alice", 30)
p.display_details()

e = Employee("Bob", 40, 50000)
e.display_details()
