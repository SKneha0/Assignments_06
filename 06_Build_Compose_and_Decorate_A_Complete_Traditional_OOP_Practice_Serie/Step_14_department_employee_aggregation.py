class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Employee object reference

    def display_department(self):
        print(f"Department: {self.department_name}")
        self.employee.display()

# Example usage
employee1 = Employee("John Doe", "Software Engineer")
department1 = Department("IT Department", employee1)

department1.display_department()
