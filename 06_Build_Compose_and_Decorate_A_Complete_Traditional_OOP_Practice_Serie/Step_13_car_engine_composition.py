class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition

    def start_car(self):
        print("Starting the car...")
        self.engine.start()

# Example usage
engine = Engine()
my_car = Car(engine)
my_car.start_car()
