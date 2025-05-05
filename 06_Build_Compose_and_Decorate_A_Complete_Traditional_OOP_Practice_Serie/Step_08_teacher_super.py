class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent class constructor
        self.subject = subject

    def display(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")

# Example usage
teacher1 = Teacher("Neha", "Mathematics")
teacher1.display()
