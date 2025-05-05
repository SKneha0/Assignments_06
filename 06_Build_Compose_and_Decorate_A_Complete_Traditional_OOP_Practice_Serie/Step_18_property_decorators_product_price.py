class Product:
    def __init__(self, price):
        self._price = price

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price can't be negative!")
        else:
            self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Price is being deleted!")
        del self._price

# Example usage
product = Product(100)

# Accessing price using getter
print("Price:", product.price)

# Setting a new price
product.price = 150
print("Updated Price:", product.price)

# Deleting the price
del product.price

# Trying to access deleted price
try:
    print(product.price)
except AttributeError:
    print("Price has been deleted.")
