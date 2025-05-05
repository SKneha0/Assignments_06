class Student:
    def __init__(self, name, marks):
        self.name = name        # object ka name set karo
        self.marks = marks      # object ka marks set karo

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

# Example usage
student1 = Student("Neha", 75)
student1.display()
