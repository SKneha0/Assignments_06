class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):  # public method
        print(f"{self.brand} is starting...")

# Example usage
my_car = Car("Toyota")

# Accessing public variable and method from outside
print("Car Brand:", my_car.brand)
my_car.start()
