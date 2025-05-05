class Logger:
    def __init__(self):
        print("Logger started")

    def __del__(self):
        print("Logger ended")

# Example usage
logger1 = Logger()

# Force deletion (optional)
del logger1