class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # public
        self._salary = salary       # protected
        self.__ssn = ssn            # private

# Create object
emp = Employee("Neha", 50000, "123-45-6789")

# Access public variable
print("Name (public):", emp.name)

# Access protected variable
print("Salary (_protected):", emp._salary)

# Try accessing private variable
try:
    print("SSN (__private):", emp.__ssn)
except AttributeError as e:
    print("Can't access __ssn directly:", e)

# Accessing private variable using name mangling (not recommended, but possible)
print("Accessing private using name mangling:", emp._Employee__ssn)
