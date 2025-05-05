# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Function to be decorated
@log_function_call
def say_hello():
    print("Hello!")

# Example usage
say_hello()
