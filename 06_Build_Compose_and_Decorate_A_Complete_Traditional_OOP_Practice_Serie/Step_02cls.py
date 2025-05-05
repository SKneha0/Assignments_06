class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # jab bhi object banega, count badhega

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()