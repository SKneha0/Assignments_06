class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    # __call__ method to make the object callable
    def __call__(self, number):
        return number * self.factor

# Example usage
multiplier = Multiplier(5)

# Testing callable() function
print(callable(multiplier))  # Should print True

# Calling the object like a function
result = multiplier(10)  # This will invoke __call__() method
print("Result:", result)  # Should print 50 (10 * 5)
