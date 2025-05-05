class Countdown:
    def __init__(self, start):
        self.start = start
    
    # Implementing __iter__() to return the iterator object
    def __iter__(self):
        self.current = self.start  # Initialize the current value
        return self
    
    # Implementing __next__() to return the next value in the countdown
    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current + 1
        else:
            raise StopIteration  # Stop iteration when countdown reaches 0

# Example usage
countdown = Countdown(5)

# Using Countdown in a for loop
for number in countdown:
    print(number)
