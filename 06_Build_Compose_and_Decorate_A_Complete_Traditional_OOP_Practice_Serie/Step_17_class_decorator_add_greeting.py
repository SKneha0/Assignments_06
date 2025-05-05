# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Adding the greet method to the class
    return cls

# Applying the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
person = Person("John")
print(person.greet())  # Should print "Hello from Decorator!"
