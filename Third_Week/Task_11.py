class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        if self.number2 == 0:
            return "Error: Cannot divide by zero"
        return self.number1 / self.number2

# Example usage:
calc = Calculator(10, 5)
print(calc.add())        # Output: 15
print(calc.subtract())   # Output: 5
print(calc.multiply())   # Output: 50
print(calc.divide())     # Output: 2.0
